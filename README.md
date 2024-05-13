
# Real-time Stock Prediction System

## Description
This repository hosts a real-time stock prediction system that fetches financial data from the Alpha Vantage API using Apache Kafka and processes it using Apache Spark. The system is designed to predict stock prices daily using a linear regression model based on the last 20 days of data.

## Monthly Plans
- **75 API requests/min + 15-min delayed US market data:** $49.99/month
- **150 API requests/min + realtime US market data:** $99.99/month
- **300 API requests/min + realtime US market data:** $149.99/month
- **600 API requests/min + realtime US market data:** $199.99/month
- **1200 API requests/min + realtime US market data:** $249.99/month

## Installation
### Prerequisites
- Apache Kafka
- ZooKeeper
- Apache Spark

### Setup
#### Kafka and ZooKeeper Setup
1. **Start ZooKeeper**:
   ```bash
   bin/zookeeper-server-start.sh config/zookeeper.properties
Start Kafka Server:
bash
Copy code
bin/kafka-server-start.sh config/server.properties
Create Kafka Topics
bash
Copy code
bin/kafka-topics.sh --create --topic social-media-data --bootstrap-server localhost:9092 --replication-factor 1 --partitions 1
bin/kafka-topics.sh --create --topic alpha-vantage-data --bootstrap-server localhost:9092 --replication-factor 1 --partitions 1
Verify Data Transmission
bash
Copy code
bin/kafka-console-consumer.sh --topic alpha-vantage-data --from-beginning --bootstrap-server localhost:9092
Spark Model Training and Prediction
Train the Model: Run the model_training.py script initially to train your model using historical data.
Start Data Production: Execute producer.py to begin data collection and processing.
Run Predictions: Use prediction.py to predict daily stock prices.
Usage
For short interval iterations, such as every 2 minutes, upgrade to a premium Alpha Vantage plan and adjust the sleep time in producer.py along with the necessary code adjustments for more frequent data fetching and processing. Ensure to train the model with more extensive data for better accuracy.

Notes
Ensure all paths and configurations are correctly set based on your environment setup.
Check Kafka and ZooKeeper are up and running before starting the Kafka server and the Spark jobs.
css
Copy code

### Instructions for GitHub
1. **Create a new file** in your GitHub repository.
2. Name it `README.md`.
3. Paste the markdown content provided above.
4. Commit the file to your repository.

This README provides a clear guide for setting up and using your stock prediction system. Adjust the content as needed to fit your specific setup or additional details you wish to include.
