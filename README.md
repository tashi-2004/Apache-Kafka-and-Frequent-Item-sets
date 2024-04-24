# Apache-Kafka-and-Frequent-Item-sets
# Overview
This project implements a streaming pipeline for processing and analyzing the Amazon Metadata dataset using various techniques such as sampling, preprocessing, frequent itemset mining, and database integration.
# Why this project?
This project is designed to:
Process and analyze the Amazon Metadata dataset in real-time using a streaming pipeline
Discover frequent itemsets in the dataset using algorithms like Apriori and PCY
Optimize data processing using the Bloom Filter data structure
Store and visualize the results in a MongoDB Compass database
Handle large datasets and scale the processing using Kafka
Perform real-time analytics and gain insights from the dataset
Preprocess the dataset to prepare it for analysis
Use multiple consumer applications to perform different tasks and analysis on the data stream
# Files
sampling.py: Python script for sampling the Amazon Metadata dataset.
pre-processing.py: Python script for preprocessing the sampled dataset.
producer.py: Python script for the producer application in the streaming pipeline setup.
consumer1.py, consumer2.py, consumer3.py: Python scripts for the consumer applications subscribing to the producer's data stream.
Apriori.py, PCY.py: Python scripts implementing the Apriori and PCY algorithms for frequent itemset mining.
Bloomfilter.py: Python script for implementing the Bloom Filter data structure.
database_apriori,PCY,BloomFilter.py: Python script for integrating with the MongoDB Compass database.
# Description
 Sampling and Preprocessing
The sampling.py script samples the Amazon Metadata dataset, followed by preprocessing using pre-processing.py.
Streaming Pipeline Setup
The producer.py script generates a data stream, while consumer1.py, consumer2.py, and consumer3.py subscribe to this stream to perform various tasks.
Frequent Itemset Mining
Apriori.py and PCY.py implement different algorithms for frequent itemset mining, while Bloomfilter.py provides support for efficient data processing.
Database Integration
The database_integration.py script connects to a MongoDB Compass database and stores the results of the analysis.
MongoDB Compass
The output generated by database_apriori,PCY,BloomFilter.py can be viewed in MongoDB Compass after integration with the MongoDB database.
Analysis
This project performs simple analysis on the dataset, including:
Frequent itemset mining using Apriori and PCY algorithms

# Usage
Run sampling.py followed by pre-processing.py to sample and preprocess the dataset.
Run producer.py to start the data stream.
Run consumer1.py, consumer2.py, and consumer3.py to subscribe to the data stream and perform analysis.
Optionally, run Apriori.py, PCY.py, and Bloomfilter.py for additional analysis.
Run database_integration.py to integrate with the MongoDB database.
# Requirements
Python 3.x
Kafka
MongoDB Compass & MongoDB Connector
Other dependencies as specified in the codes
# Note
Kindly, remove numbers at the start of the files e.g, Change 3) producer.py to producer.py. They are just given for clarifications. Thank You! 
