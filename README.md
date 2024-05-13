# Real-time Stock Prediction System

## Description
This repository hosts a real-time stock prediction system that fetches financial data from the Alpha Vantage API using Apache Kafka and processes it using Apache Spark. The system is designed to predict stock prices **daily** using a linear regression model based on the last 20 days of data.

## Installation
### Prerequisites
- Apache Kafka
- ZooKeeper
- Apache Spark

### Setup
#### Kafka and ZooKeeper Setup
1. **Start ZooKeeper**:
 
   bin/zookeeper-server-start.sh config/zookeeper.properties
2.  **Start Kafka Server**:
   bin/kafka-server-start.sh config/server.properties
3. **Create Kafka Topics**:
  - bin/kafka-topics.sh --create --topic social-media-data --bootstrap-server localhost:9092 --replication-factor 1 --partitions 1
  - bin/kafka-topics.sh --create --topic alpha-vantage-data --bootstrap-server localhost:9092 --replication-factor 1 --partitions 1
    
4.**Verify Data Transmission**:
   - bin/kafka-console-consumer.sh --topic alpha-vantage-data --from-beginning --bootstrap-server localhost:9092

#### Spark Model Training and Prediction
1. **Train the Model**:
   - Run the `model_training.py` script initially to train your model using historical data.
   - - Alternatively, use Google Colab for training by opening and running the `Stock_prediction_on_spark.ipynb` notebook which is detailed and ready for execution.



2. **Run Predictions**:
   - Use `prediction.py` to predict daily stock prices.
   - <img width="789" alt="image" src="https://github.com/Bike001/Real-time-stock-prediciton-/assets/114451652/930fc415-a84a-4e89-9a51-11b9ea9318ca">
   <img width="776" alt="image" src="https://github.com/Bike001/Real-time-stock-prediciton-/assets/114451652/debc100d-4fd6-4b90-b703-f8168a4cd206">


3. **Start Data Production**:
   - Execute `producer.py` to begin data collection and processing.
   - <img width="793" alt="image" src="https://github.com/Bike001/Real-time-stock-prediciton-/assets/114451652/a2aa6fb6-2f5c-4a88-9d4d-e6d848c164a9">


#### Usage
For short interval iterations, such as every 2 minutes, upgrade to a premium Alpha Vantage plan and adjust the sleep time in producer.py along with the necessary code adjustments for more frequent data fetching and processing. Ensure to train the model with more extensive data for better accuracy.

## Monthly Plans
- **75 API requests/min + 15-min delayed US market data:** $49.99/month
- **150 API requests/min + realtime US market data:** $99.99/month
- **300 API requests/min + realtime US market data:** $149.99/month
- **600 API requests/min + realtime US market data:** $199.99/month
- **1200 API requests/min + realtime US market data:** $249.99/month

### Notes
Ensure all paths and configurations are correctly set based on your environment setup.
Check Kafka and ZooKeeper are up and running before starting the Kafka server and the Spark jobs.


