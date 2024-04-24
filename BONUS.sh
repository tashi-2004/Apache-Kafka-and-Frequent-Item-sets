#!/bin/bash

# Function to start Zookeeper
start_zookeeper() {
    echo "Starting Zookeeper..."
    gnome-terminal -- /bin/bash -c "cd kafka && bin/zookeeper-server-start.sh config/zookeeper.properties; exec bash" &
}

# Function to start Kafka Server after Zookeeper has been running for 10 seconds
start_kafka_server() {
    echo "Waiting for Zookeeper to stabilize..."
    sleep 10
    echo "Starting Kafka Server..."
    while true; do
        gnome-terminal -- /bin/bash -c "cd kafka && bin/kafka-server-start.sh config/server.properties; exec bash" &
        sleep 10 # Retry every 10 seconds
        # Check if Kafka server is still running, if not retry
        if ! pgrep -f "kafka\.Kafka" >/dev/null; then
            echo "Kafka Server stopped unexpectedly. Retrying..."
        else
            break
        fi
    done
}

# Function to start the producer script after Kafka Server has been running for 20 seconds
start_producer() {
    echo "Waiting 20 seconds before starting Producer..."
    sleep 10
    echo "Starting Producer..."
    gnome-terminal -- /bin/bash -c "python3 producer.py; exec bash" &
}

# Function to start consumer scripts after Kafka Server has been running for 30 seconds
start_consumers() {
    echo "Waiting 30 seconds before starting Consumers..."
    sleep 10
    echo "Starting Consumer 1..."
    gnome-terminal -- /bin/bash -c "python3 consumer1.py; exec bash" &
    sleep 10
    echo "Starting Consumer 2..."
    gnome-terminal -- /bin/bash -c "python3 consumer2.py; exec bash" &
    sleep 10
    echo "Starting Consumer 3..."
    gnome-terminal -- /bin/bash -c "python3 consumer3.py; exec bash" &
}

# Function to start additional scripts after the previous components
start_additional_scripts() {
    echo "Waiting 40 seconds before starting additional scripts..."
    sleep 10
    echo "Starting Apriori.py..."
    gnome-terminal -- /bin/bash -c "python3 Apriori.py; exec bash" &
    sleep 10
    echo "Starting PCY.py..."
    gnome-terminal -- /bin/bash -c "python3 PCY.py; exec bash" &
    sleep 10
    echo "Starting Bloomfilter.py..."
    gnome-terminal -- /bin/bash -c "python3 Bloomfilter.py; exec bash" &
}

# Function to start database scripts after the additional scripts
start_database_scripts() {
    echo "Waiting 50 seconds before starting database scripts..."
    sleep 10
    echo "Starting Database_Apriori.py..."
    gnome-terminal -- /bin/bash -c "python3 Database_Apriori.py; exec bash" &
    sleep 10
    echo "Starting Database_PCY.py..."
    gnome-terminal -- /bin/bash -c "python3 Database_PCY.py; exec bash" &
    sleep 10
    echo "Starting Database_Bloomfilter.py..."
    gnome-terminal -- /bin/bash -c "python3 Database_Bloomfilter.py; exec bash" &
}

# Main function to orchestrate project execution
main() {
    start_zookeeper
    start_kafka_server
    start_producer
    start_consumers
    start_additional_scripts
    start_database_scripts
}

# Calling the main function to start the project execution
main

