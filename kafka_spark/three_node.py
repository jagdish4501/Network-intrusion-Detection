import concurrent.futures
import time
import os
import numpy as np
import pandas as pd
import joblib
import json
from kafka import KafkaConsumer
import joblib
Random_Forest = joblib.load('./Random_forest_cicids.pkl')

print("procss id :", os.getpid())

start = time.time()


def task_1():
    print("process id:", os.getpid())
    kafka_topic = "node_1"
    consumer = KafkaConsumer(
        kafka_topic,
        bootstrap_servers='localhost:9092',
        auto_offset_reset='latest',
        enable_auto_commit=True,
        group_id='my-group'
    )

    try:
        for messages in consumer:
            values = messages.value.decode('utf-8')
            df = pd.read_csv(pd.io.common.StringIO(values))
            Xn = df.drop([' Label'], axis=1)
            Yn = df[' Label'].values[0]
            Predict_X = Random_Forest.predict(Xn)
            print(f"node_1", Predict_X[0], Yn,
                  'time : ', time.time()-start, "second")

    except KeyboardInterrupt:
        print("KeyboardInterrupt: Stopping the consumer loop in task1 .")
    finally:
        consumer.close()


def task_2():
    print("process id:", os.getpid())
    kafka_topic = "node_2"
    consumer = KafkaConsumer(
        kafka_topic,
        bootstrap_servers='localhost:9092',
        auto_offset_reset='latest',
        enable_auto_commit=True,
        group_id='my-group'
    )

    try:
        for messages in consumer:
            values = messages.value.decode('utf-8')
            df = pd.read_csv(pd.io.common.StringIO(values))
            Xn = df.drop([' Label'], axis=1)
            Yn = df[' Label'].values[0]
            Predict_X = Random_Forest.predict(Xn)
            print(f"node_2", Predict_X[0], Yn,
                  'time : ', time.time()-start, "second")

    except KeyboardInterrupt:
        print("KeyboardInterrupt: Stopping the consumer loop in taks 2.")
    finally:
        consumer.close()


def task_3():
    print("process id:", os.getpid())
    kafka_topic = "node_3"
    consumer = KafkaConsumer(
        kafka_topic,
        bootstrap_servers='localhost:9092',
        auto_offset_reset='latest',
        enable_auto_commit=True,
        group_id='my-group'
    )

    try:
        for messages in consumer:
            values = messages.value.decode('utf-8')
            df = pd.read_csv(pd.io.common.StringIO(values))
            Xn = df.drop([' Label'], axis=1)
            Yn = df[' Label'].values[0]
            Predict_X = Random_Forest.predict(Xn)
            print(f"node_3", Predict_X[0], Yn,
                  'time : ', time.time()-start, "second")

    except KeyboardInterrupt:
        print("KeyboardInterrupt: Stopping the consumer loop in task 3.")
    finally:
        consumer.close()


if __name__ == "__main__":
    try:
        with concurrent.futures.ProcessPoolExecutor() as executor:
            future_1 = executor.submit(task_1)
            future_2 = executor.submit(task_2)
            future_3 = executor.submit(task_3)
            concurrent.futures.wait([future_1, future_2, future_3])

    except KeyboardInterrupt:
        print("KeyboardInterrupt: terminating all process")

    print("All tasks completed")
