#Tashfeen Abbasi
#Laiba Mazhar
#Rafia Khan
#Apache-Kafka-and-Frequent-Item-sets
from kafka import KafkaProducer
import json
import time

#Preprocessed record
def preprocess(record):
    return record

#Stream Data
def streaming(file_path, topic_name):
    producer = KafkaProducer(bootstrap_servers='localhost:9092',
                             value_serializer=lambda v: json.dumps(v).encode('utf-8'))

    with open(file_path, 'r') as infile:
        for i in infile:
            record = json.loads(i.strip())
            processed_record = preprocess(record)
            producer.send(topic_name, value=processed_record)
            time.sleep(0.1) 
    producer.flush()
    producer.close()



#Entry point
if __name__ == "__main__":
    file_path ='/home/laibu/preprocessed_data.json'
    topic_name = 'assignment'
    streaming(file_path, topic_name)
