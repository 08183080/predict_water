import numpy as np
import pandas as pd
from datetime import datetime

excel_file = 'input.xlsx'  
res = 'output.xlsx'

def get_data():
    df = pd.read_excel(excel_file)
    print(df.columns)
    print(df)

def update_date():
    df = pd.read_excel(excel_file)
    df['测量日期'] = df['测量日期'].apply(lambda x: datetime.strptime(x, '%Y/%m/%d').replace(year=2023).strftime('%Y/%m/%d'))
    # print(df)
    df.to_excel(res, index=False)

def random_data():
    df = pd.read_excel(res)
    columns = list(df.columns)[2:]

    df[columns] = df[columns].apply(pd.to_numeric, errors='coerce')
    # print(columns)    

    k = np.random.uniform(0.8, 1.4)
    df[columns] *= k
    # print(df[0:10])

    df.to_excel(res, index=False)

def after_rain_9():
    """
    update month 9
    """
    df = pd.read_excel(res)
    
    mask = df['测量日期'] == '2023/10/04'
    selected_rows = df[mask]

    columns_to_adjust = list(df.columns)[2:]
    k = np.random.uniform(1, 1.4)
    selected_rows[columns_to_adjust] *= k
    
    df[mask] = selected_rows
    # print(df[mask])
    df.to_excel(res, index=False)

    
if __name__ == "__main__":
    # get_data()
    # update_date()
    # random_data()
    after_rain_9()
    # get_data()

