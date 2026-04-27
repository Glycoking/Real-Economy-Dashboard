import requests
import pandas as pd
import numpy as np


def api_call(url:str):
    response = requests.api.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        raise ValueError("API call failed, check URL is correct and working")
    

def get_data(url:str) -> pd.DataFrame:
    data = api_call(url)
    data_normalized = pd.json_normalize(data[1]) 
    return data_normalized

def clean_data(data:pd.DataFrame, na=True)-> pd.DataFrame:
    column_to_drop = ["decimal","obs_status", "countryiso3code","country.id","indicator.value","indicator.id","unit"]
    data = data.drop(columns=column_to_drop)
    if na == True: 
        data= data.dropna()
    data = data.rename(columns={"date":"Year","value": "GDP", "country.value":"Country" })
    
    return data

url = "https://api.worldbank.org/v2/country/all/indicator/NY.GDP.MKTP.CD?format=json&per_page=20000"
data = get_data(url)
data = clean_data(data, na=False)

print(data.sample(20))
#print(data.info())
