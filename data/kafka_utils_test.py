import pandas as pd
from kafka_utils import KafkaStreamer
from kafka.errors import NoBrokersAvailable

# Assuming the KafkaStreamer class is already imported from the relevant file

def test_kafka_streamer():
    # Sample Kafka broker address
    broker_address = 'localhost:9092'  # Update this if your Kafka broker address is different

    # Create a sample DataFrame
    sample_data = {
        'id': [1, 2, 3],
        'name': ['Alice', 'Bob', 'Charlie'],
        'age': [25, 30, 35]
    }
    sample_df = pd.DataFrame(sample_data)

    # Create an instance of KafkaStreamer
    kafka_streamer = KafkaStreamer(broker_address)

    # Specify Kafka topic
    topic = 'test_topic'

    try:
        # Produce the DataFrame to Kafka
        kafka_streamer.produce_dataframe(topic, sample_df)
        print("Data has been successfully streamed to Kafka.")
    except NoBrokersAvailable:
        print("Kafka broker is not available. Please check if Kafka is running and the broker address is correct.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    test_kafka_streamer()
