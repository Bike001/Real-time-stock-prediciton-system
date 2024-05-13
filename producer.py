import json
import requests
from kafka import KafkaProducer
from time import sleep

# Initialize the Kafka producer
producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
                         value_serializer=lambda x: json.dumps(x).encode('utf-8'))

# Alpha Vantage API details
api_key = 'S2YI6J8LUGFZAX9E'
function = 'TIME_SERIES_DAILY'
symbol = 'AAPL'
outputsize = 'full'  # Fetch full historical data

# Fetch and process data
url = f"https://www.alphavantage.co/query?function={function}&symbol={symbol}&outputsize={outputsize}&apikey={api_key}"
response = requests.get(url)
data = response.json()

if 'Time Series (Daily)' in data:
    # Extract the time series data
    daily_data = data['Time Series (Daily)']
    # Sort keys to get the latest 100 trading days
    trading_days = sorted(daily_data.keys(), reverse=True)[:100]
    filtered_data = {day: daily_data[day] for day in trading_days}

    # Convert data to match your LSTM input format
    lstm_input = []
    for date in trading_days:
        daily_values = daily_data[date]
        formatted_data = [
            float(daily_values['1. open']),
            float(daily_values['2. high']),
            float(daily_values['3. low']),
            float(daily_values['4. close']),
            int(daily_values['5. volume'])
        ]
        lstm_input.append(formatted_data)

    # Send data to Kafka topic
    producer.send('alpha-vantage-data', value=json.dumps(lstm_input))
    producer.flush()
    print("Data sent to Kafka topic 'alpha-vantage-data'")
else:
    print("Failed to fetch data or data is empty", data.get("Note", data.get("Information", "No additional info provided.")))

# You can set this to a regular interval, e.g., daily, to continuously update the dataset
sleep(86400)  # Sleep for a day
