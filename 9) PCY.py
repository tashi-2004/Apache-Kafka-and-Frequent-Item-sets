from kafka import KafkaConsumer
import json
from collections import defaultdict
from itertools import combinations

def hash_bucket(itemset, num_buckets):
    return hash(frozenset(itemset)) % num_buckets

def calculate_hash_counts(data, hash_buckets):
    hash_counts = defaultdict(int)
    for transaction in data:
        for pair in combinations(transaction, 2):
            bucket = hash_bucket(pair, hash_buckets)
            hash_counts[bucket] += 1
    return hash_counts

def generate_candidates(prev_freq_itemsets, k, hash_counts, hash_buckets, threshold):
    candidates = set()
    for itemset1 in prev_freq_itemsets:
        for itemset2 in prev_freq_itemsets:
            if len(itemset1.union(itemset2)) == k:
                candidate = itemset1.union(itemset2)
                if is_candidate_frequent(candidate, k, hash_counts, hash_buckets, threshold):
                    candidates.add(candidate)
    return candidates

# Function to check if a candidate itemset is frequent using hashed counts
def is_candidate_frequent(candidate, k, hash_counts, hash_buckets, threshold):
    subsets = combinations(candidate, k-1)
    for subset in subsets:
        bucket = hash_bucket(subset, hash_buckets)
        if hash_counts[bucket] < threshold:
            return False
    return True

def calculate_support(data, itemsets):
    support_count = defaultdict(int)
    for transaction in data:
        for itemset in itemsets:
            if itemset.issubset(transaction):
                support_count[itemset] += 1
    return support_count

def process_message(message, window_size, min_support, hash_counts, hash_buckets, threshold):
    global transaction_window
    data = message.value
    transaction_window.append(data)
    
    if len(transaction_window) >= window_size:
        hash_counts = calculate_hash_counts(transaction_window, hash_buckets)
        frequent_itemsets = generate_frequent_itemsets(transaction_window, min_support, hash_counts, hash_buckets, threshold)
        
        print("______________________")
        print("| Frequent Itemsets  |")
        print("|____________________|")
        for itemset in frequent_itemsets:
            items = [str(data[column]) for column in itemset if column in data]
            if items:
                filtered_items = [item for item in items if not (item.startswith('http') or '<' in item or '>' in item)]
                if filtered_items:
                    print(filtered_items[0])
        del transaction_window[0]
def generate_frequent_itemsets(data, min_support, hash_counts, hash_buckets, threshold):
    itemsets = [frozenset([item]) for transaction in data for item in transaction]
    freq_itemsets = []
    k = 1

    while itemsets:
        support_count = calculate_support(data, itemsets)
        freq_itemsets.extend([itemset for itemset, support in support_count.items() if support >= min_support])
        candidates = generate_candidates(set(freq_itemsets), k+1, hash_counts, hash_buckets, threshold)
        itemsets = candidates
        k += 1

    return freq_itemsets

topic_name = 'assignment'
window_size = 100  
min_support = 2   
hash_buckets = 1000 
threshold = 2 
hash_counts = defaultdict(int) 
transaction_window = []

consumer = KafkaConsumer(topic_name, bootstrap_servers='localhost:9092',
                         value_deserializer=lambda x: json.loads(x.decode('utf-8')))

for message in consumer:
    process_message(message, window_size, min_support, hash_counts, hash_buckets, threshold)

