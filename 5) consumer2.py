
#Tashfeen Abbasi
#Laiba Mazhar
#Rafia Khan
#Apache-Kafka-and-Frequent-Item-sets
from kafka import KafkaConsumer
import json

topic_name = 'assignment'

consumer = KafkaConsumer(topic_name, bootstrap_servers='localhost:9092', group_id='group2',
                         value_deserializer=lambda x: json.loads(x.decode('utf-8')))

for message in consumer:
    print(f"Consumer 2 received message: {message.value}")
