import csv
from kafka import KafkaProducer
import time
import pandas as pd
df = pd.read_csv('./data_for_kafka.csv', nrows=0)


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
    start = time.time()
    with open(input_file, newline='') as csvfile:
        csv_reader = csv.reader(csvfile)
        for i, row in enumerate(csv_reader):
            if i == 10000:
                break
            if i != 0:
                message = pd.DataFrame([row], columns=df.columns)
                # Convert DataFrame to string
                message_str = message.to_csv(index=False)
                # print(f"message {i}:", message_str)
                topic1 = "single_node_"+str(1)
                producer.send(topic1, value=message_str).add_callback(
                    delivery_report)
    print("Time Taken :", time.time()-start, "second")
    producer.flush()


if __name__ == '__main__':
    input_csv_file = './data_for_kafka_suffled.csv'
    kafka_producer(input_csv_file)
