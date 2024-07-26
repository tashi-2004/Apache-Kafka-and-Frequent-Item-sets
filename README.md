# Apache-Kafka-and-Frequent-Itemsets

## Overview
This project implements a streaming pipeline for processing and analyzing the Amazon Metadata dataset using various techniques such as sampling, preprocessing, frequent itemset mining, and database integration.

## Why this project?
This project is designed to:
- Process and analyze the Amazon Metadata dataset in real-time using a streaming pipeline
- Discover frequent itemsets in the dataset using algorithms like Apriori and PCY
- Optimize data processing using the Bloom Filter data structure
- Store and visualize the results in a MongoDB Compass database
- Handle large datasets and scale the processing using Kafka
- Perform real-time analytics and gain insights from the dataset
- Preprocess the dataset to prepare it for analysis
- Use multiple consumer applications to perform different tasks and analyses on the data stream

## Files
- `sampling.py`: Python script for sampling the Amazon Metadata dataset.
- `pre-processing.py`: Python script for preprocessing the sampled dataset.
- `producer.py`: Python script for the producer application in the streaming pipeline setup.
- `consumer1.py`, `consumer2.py`, `consumer3.py`: Python scripts for the consumer applications subscribing to the producer's data stream.
- `Apriori.py`: Python script implementing the Apriori algorithm for frequent itemset mining.
- `PCY.py`: Python script implementing the PCY algorithm for frequent itemset mining.
- `Bloomfilter.py`: Python script for implementing the Bloom Filter data structure.
- `Database_Apriori.py`: Python script for integrating Apriori results with the MongoDB Compass database.
- `Database_PCY.py`: Python script for integrating PCY results with the MongoDB Compass database.
- `Database_Bloomfilter.py`: Python script for integrating Bloom Filter results with the MongoDB Compass database.

## Description
### Sampling and Preprocessing
The `sampling.py` script samples the Amazon Metadata dataset, followed by preprocessing using `pre-processing.py`.

### Streaming Pipeline Setup
The `producer.py` script generates a data stream, while `consumer1.py`, `consumer2.py`, and `consumer3.py` subscribe to this stream to perform various tasks.

### Frequent Itemset Mining
`Apriori.py` and `PCY.py` implement different algorithms for frequent itemset mining, while `Bloomfilter.py` provides support for efficient data processing.

### Database Integration
The `Database_Apriori.py`, `Database_PCY.py`, and `Database_Bloomfilter.py` scripts connect to a MongoDB Compass database and store the results of the analysis.

### MongoDB Compass
The output generated by `Database_Apriori.py`, `Database_PCY.py`, and `Database_Bloomfilter.py` can be viewed in MongoDB Compass after integration with the MongoDB database.

### Analysis
This project performs simple analysis on the dataset, including:
- Frequent itemset mining using Apriori and PCY algorithms

## Usage
1. Run `sampling.py` followed by `pre-processing.py` to sample and preprocess the dataset.
2. Run `producer.py` to start the data stream.
3. Run `consumer1.py`, `consumer2.py`, and `consumer3.py` to subscribe to the data stream and perform analysis.
4. Optionally, run `Apriori.py`, `PCY.py`, and `Bloomfilter.py` for additional analysis.
5. Run `Database_Apriori.py`, `Database_PCY.py`, and `Database_Bloomfilter.py` to integrate with the MongoDB database.

## Requirements
- Python 3.x
- Kafka
- MongoDB Compass & MongoDB Connector
- Other dependencies as specified in the code

## Note
- Kindly, remove numbers at the start of the files (e.g., change `(3) producer.py` to `producer.py`). They are just given for clarifications.
- Run the `BONUS.sh` file on the terminal with the command `./BONUS.sh`.

## Contributors
- M.Tashfeen Abbasi
- [Laiba Mazhar](https://github.com/laiba-mazhar)
- [Rafia Khan](https://github.com/rakhan2)

Thank you!
