# -*- coding: utf-8 -*-
"""
Created on Sun Feb 19 15:24:39 2023

@author: himan
"""
""" Python Extract Transform Load example """

import requests 
import pandas as pd
from sqlalchemy import create_engine

#request libraries help to pull data from an API that further extracts the data
#pandas are used to transform and manipulate the data. Pandas can also transform CSV data. 
#SQLAlchemy helps support to create connection to a database like SQLite.

#we will use the function below to extract the data

def extract() -> dict:
    """ This API extracts data from
    http://universities.hipolabs.com
    """
    API_URL = "http://universities.hipolabs.com/search?country=United+States"
    data = requests.get(API_URL).json()
    return data

#we will transform the data in the right format and sequence

def transform(data:dict) -> pd.DataFrame:
  """ Transforms the dataset into desired structure and filters"""
  df = pd.DataFrame(data)
  print(f"Total Number of Universities from API {len(data)}")
  df['domains'] = [','.join(map(str, l)) for l in df['domains']]
  df['web_pages'] = [','.join(map(str, l)) for l in df['web_pages']]
  df = df.reset_index(drop=True)
  return df[["domains","country","web_pages","name"]]

def load(df:pd.DataFrame)-> None:
    """ Loads data into a sqllite database"""
    disk_engine = create_engine('sqlite:///my_lite_store.db')
    df.to_sql('cal_uni', disk_engine, if_exists='replace')
    
data = extract()
df = transform(data)
load(df) 

