import csv
from kafka import KafkaProducer
import time
import pandas as pd

PATH='../pcapture/packet_features.csv'
df = pd.read_csv('./testing_data.csv', nrows=0)
df = df.drop(columns=[' Label'])


def delivery_report(err, msg):
    if err is not None:
        print('Message delivery failed: {}'.format(err))
    else:
        print('Message delivered to {} [{}]'.format(
            msg.topic(), msg.partition()))


def kafka_producer(input_file, kafka_bootstrap_servers='localhost:9092'):
    # Kafka producer configuration
    producer = KafkaProducer(
        bootstrap_servers=kafka_bootstrap_servers,
        value_serializer=str.encode
    )
    while True:
        try:
            with open(input_file, newline='') as csvfile:
                csv_reader = csv.reader(csvfile)
                for i, row in enumerate(csv_reader):
                    if i != 0:
                        message = pd.DataFrame([row], columns=df.columns)
                        # Convert DataFrame to string
                        message_str = message.to_csv(index=False)
                        print(f"message {i}:", message_str)
                        topic1 = "single_node_1"
                        producer.send(topic1, value=message_str).add_callback(
                            delivery_report)
            producer.flush()
            time.sleep(5)   
        except Exception as e:
            print('something went wrong-kafka_producer-function',e)
            time.sleep(5)


if __name__ == '__main__':
    kafka_producer(PATH)
