import json
from kafka import KafkaConsumer
from pyspark.ml import PipelineModel
from pyspark.sql import Row, SparkSession

# Function to load the trained model
def load_model(model_path):
    return PipelineModel.load(model_path)

# Function to perform prediction
def predict_new_data(model, new_data):
    spark = SparkSession.builder.master("local[*]").appName("StockPricePrediction").getOrCreate()
    sample_data = spark.createDataFrame([new_data])
    predictions = model.transform(sample_data)
    predictions.select("prediction").show()

# Initialize Kafka Consumer
consumer = KafkaConsumer(
    'alpha-vantage-data',
    bootstrap_servers=['localhost:9092'],
    auto_offset_reset='latest',
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

# Load the model
model_path = "/Users/yusoo/Downloads/kafka_2.13-3.7.0/stock/mymodel"
model = load_model(model_path)

# Consumer loop to fetch data and make predictions
try:
    print("Listening for messages on topic: 'alpha-vantage-data'")
    for message in consumer:
        # print("Raw data received:", message.value)
        data = json.loads(message.value)  # Ensure data is loaded as a JSON object
        if len(data) >= 20:
            try:
                open_prices = [float(day[0]) for day in data[-20:]]
                new_data = Row(**{f"lag_{i+1}": open_prices[i] for i in range(20)})
                predict_new_data(model, new_data)
            except ValueError as e:
                print("Error converting data:", e)
finally:
    # Ensure to close the consumer after fetching data
    consumer.close()
    print("Consumer closed.")

