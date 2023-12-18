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

start = time.time()


def task_1():
    print("process id:", os.getpid())
    kafka_topic = "single_node_1"
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
            print(f"single node executor :", Predict_X[0], Yn,
                  'time : ', time.time()-start, "second")

    except KeyboardInterrupt:
        print("KeyboardInterrupt: Stopping the consumer loop in task1 .")
    finally:
        consumer.close()


if __name__ == "__main__":
    try:
        task_1()
    except KeyboardInterrupt:
        print("KeyboardInterrupt: terminating all process")

    print("All tasks completed")
