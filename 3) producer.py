
#Tashfeen Abbasi
#Laiba Mazhar
#Rafia Khan
#Apache-Kafka-and-Frequent-Item-sets
from kafka import KafkaProducer
import json
import time

#Preprocess_record
def preprocess_record(record):
    return record

#Stream-data function
def stream_data(file_path, topic_name):
    producer = KafkaProducer(bootstrap_servers='localhost:9092',
                             value_serializer=lambda v: json.dumps(v).encode('utf-8'))

    with open(file_path, 'r') as infile:
        for line in infile:
            record = json.loads(line.strip())
            processed_record = preprocess_record(record)
            producer.send(topic_name, value=processed_record)
            time.sleep(0.1) 
    producer.flush()
    producer.close()

#Entry point
if __name__ == "__main__":
    file_path = '/home/laibu/preprocessed_data.json'
    topic_name = 'assignment'
    stream_data(file_path, topic_name)
