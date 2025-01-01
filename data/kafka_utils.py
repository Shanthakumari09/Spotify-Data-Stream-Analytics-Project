import time
import json
import pandas as pd
from kafka import KafkaProducer

class KafkaStreamer:
    '''
    Kafka Streamer class for streaming data to Kafka
    '''
    def __init__(self, broker_address: str) -> None:
        '''
        Args:
            broker_address (str): Kafka broker address
        '''
        self.producer = KafkaProducer(bootstrap_servers=[broker_address], value_serializer=lambda x: json.dumps(x).encode('utf-8'))

    def produce_dataframe(self, topic:str, dataframe: pd.DataFrame) -> bool:
        '''
        Produce data to Kafka
        Args:
            topic (str): Kafka topic name
            dataframe (pd.DataFrame): Data to be streamed
            rns:
            bool: True if data is streamed successfully
        '''
        for row in dataframe.itertuples(index=False):
            print(row)
            key_bytes = str(time.time()).encode('utf-8')

            self.producer.send(topic, key=key_bytes, value=row)
            time.sleep(0.5)

        self.producer.flush()