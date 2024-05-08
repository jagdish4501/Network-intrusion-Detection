import pandas as pd
import time


PATH='../pcapture/packet_features.csv'

while True:
    try:
        df=pd.read_csv(PATH)
        print(df)
        time.sleep(10)
    except:
        print('some thing went wrong')
        time.sleep(5)