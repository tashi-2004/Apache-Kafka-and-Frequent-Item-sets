#Tashfeen Abbasi
#Laiba Mazhar
#Rafia Khan
#Apache-Kafka-and-Frequent-Item-sets
import json
def process_batch(batch, output_file):
    for record in batch:
        output_file.write(json.dumps(record) + '\n')

file_path = 'D:\Sampled_Amazon_Meta.json'
output_file_name = 'preprocessed_data.json'
batch_size = 100

with open(file_path, mode='r') as infile, open(output_file_name, 'w', encoding='utf-8') as outfile:
    current_batch = []
    for line in infile:
        record = json.loads(line.strip())
        #record contains the 'also_buy' key
        if record.get('also_buy'):
            extracted_data = {'asin': record['asin'], 'also_buy': record['also_buy']}
            current_batch.append(extracted_data)
            del record
        if len(current_batch) == batch_size:
            process_batch(current_batch, outfile)
            current_batch.clear()
    if current_batch:
        process_batch(current_batch, outfile)
