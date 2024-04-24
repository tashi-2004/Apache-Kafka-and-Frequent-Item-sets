#Tashfeen Abbasi
#Laiba Mazhar
#Rafia Khan
#Apache-Kafka-and-Frequent-Item-sets
from kafka import KafkaConsumer
import json
from collections import defaultdict
from itertools import combinations

def generate_candidates(prev_freq_itemsets, k):
    candidates = set()
    for itemset1 in prev_freq_itemsets:
        for itemset2 in prev_freq_itemsets:
            if len(itemset1.union(itemset2)) == k:
                candidates.add(itemset1.union(itemset2))
    return candidates

def prune_itemsets(candidates, prev_freq_itemsets, k):
    pruned_itemsets = set()
    for candidate in candidates:
        subsets = combinations(candidate, k-1)
        is_valid = True
        for subset in subsets:
            if frozenset(subset) not in prev_freq_itemsets:
                is_valid = False
                break
        if is_valid:
            pruned_itemsets.add(candidate)
    return pruned_itemsets

# Function to calculate support count for each itemset
def calculate_support(data, itemsets):
    support_count = defaultdict(int)
    for transaction in data:
        for itemset in itemsets:
            if itemset.issubset(transaction):
                support_count[itemset] += 1
    return support_count

# Function to generate frequent itemsets
def generate_frequent_itemsets(data, min_support):
    itemsets = [frozenset([item]) for transaction in data for item in transaction]
    freq_itemsets = []
    k = 1

    while itemsets:
        # Calculate support count for each itemset
        support_count = calculate_support(data, itemsets)

        # Filter itemsets based on min_support
        freq_itemsets.extend([itemset for itemset, support in support_count.items() if support >= min_support])

        # Generate candidate itemsets
        candidates = generate_candidates(set(freq_itemsets), k+1)

        # Prune candidate itemsets
        itemsets = prune_itemsets(candidates, set(freq_itemsets), k+1)

        k += 1

    return freq_itemsets
def process_message(message, window_size, min_support):
    global transaction_window
    data = message.value
    transaction_window.append(data)
    
    if len(transaction_window) >= window_size:
        del transaction_window[0]
    frequent_itemsets = generate_frequent_itemsets(transaction_window, min_support)
    print("______________________")
    print("| Frequent Itemsets  |")
    print("|____________________|")
    for itemset in frequent_itemsets:
        items = [str(data[column]) for column in itemset if column in data]  # Convert items to strings
        if items: 
            filtered_items = [item for item in items if not (item.startswith('http') or '<' in item or '>' in item)]
            if filtered_items:  
                print(filtered_items[0]) 
    print("\n\n")

topic_name = 'assignment'
window_size = 100 
min_support = 2  
transaction_window = []

consumer = KafkaConsumer(topic_name, bootstrap_servers='localhost:9092',
                         value_deserializer=lambda x: json.loads(x.decode('utf-8')))

# Consume messages 
for message in consumer:
    process_message(message, window_size, min_support)

