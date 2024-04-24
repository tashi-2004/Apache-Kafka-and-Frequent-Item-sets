#Tashfeen Abbasi
#Laiba Mazhar
#Rafia Khan
#Apache-Kafka-and-Frequent-Item-sets
from kafka import KafkaConsumer
import json
from pybloom_live import BloomFilter
from collections import defaultdict

bloom_filter_capacity = 10000  
false_positive_probability = 0.01  
bloom_filter = BloomFilter(capacity=bloom_filter_capacity, error_rate=false_positive_probability)

# process message
def process_message(message, window_size):
    global transaction_window
    data = message.value  
    if str(data) not in bloom_filter:
        bloom_filter.add(str(data))
        transaction_window.append(data)
    
        if len(transaction_window) >= window_size:
            del transaction_window[0]
        
        print("______________________")
        print("| Frequent Itemsets  |")
        print("|____________________|")
        for transaction in transaction_window:
            items = [str(data[column]) for column in transaction if column in data]  # Convert items to strings
            if items:  
                filtered_items = [item for item in items if not (item.startswith('http') or '<' in item or '>' in item)]
                if filtered_items: 
                    print(filtered_items) 
        print("\n\n")

topic_name = 'assignment'
window_size = 100 
transaction_window = []

consumer = KafkaConsumer(topic_name, bootstrap_servers='localhost:9092',
                         value_deserializer=lambda x: json.loads(x.decode('utf-8')))

# Consume messages
for message in consumer:
    process_message(message, window_size)

