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
            try:
                values = messages.value.decode('utf-8')
                Xn= pd.read_csv(pd.io.common.StringIO(values))
                Predict_X = Random_Forest.predict(Xn)
                print(f"Predicted Label : ", Predict_X,
                    'time : ', time.time()-start, "second")
            except Exception as e:
                print('something went wrong in task1_fun',e)

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
