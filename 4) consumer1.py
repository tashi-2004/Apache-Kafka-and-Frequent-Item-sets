
#Tashfeen Abbasi
#Laiba Mazhar
#Rafia Khan
#Apache-Kafka-and-Frequent-Item-sets
from kafka import KafkaConsumer
import json
from collections import defaultdict
from itertools import combinations

#generate candidate itemsets
def generate_candidates(prev_freq_itemsets, k):
    candidates = set()
    for itemset1 in prev_freq_itemsets:
        for itemset2 in prev_freq_itemsets:
            if len(itemset1.union(itemset2)) == k:
                candidates.add(itemset1.union(itemset2))
    return candidates

#prune candidate itemsets
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

#calculate support count for each itemset
def calculate_support(data, itemsets):
    support_count = defaultdict(int)
    for transaction in data:
        for itemset in itemsets:
            if itemset.issubset(transaction):
                support_count[itemset] += 1
    return support_count

#generate frequent itemsets
def generate_frequent_itemsets(data, min_support):
    itemsets = [frozenset([item]) for transaction in data for item in transaction]
    freq_itemsets = []
    k = 1

    while itemsets:
        support_count = calculate_support(data, itemsets)
        freq_itemsets.extend([itemset for itemset, support in support_count.items() if support >= min_support])
        candidates = generate_candidates(set(freq_itemsets), k+1)
        itemsets = prune_itemsets(candidates, set(freq_itemsets), k+1)

        k += 1

    return freq_itemsets

#process messages and generate insights using Apriori algorithm
def process_message(message):
    data = message.value 
    min_support = 2 
    frequent_itemsets = generate_frequent_itemsets(data, min_support)
    print("Frequent Itemsets:")
    for itemset in frequent_itemsets:
        print(itemset)

# Kafka Consumer configuration
topic_name = 'assignment'
consumer = KafkaConsumer(topic_name, bootstrap_servers='localhost:9092',
                         value_deserializer=lambda x: json.loads(x.decode('utf-8')))
for message in consumer:
    process_message(message)

