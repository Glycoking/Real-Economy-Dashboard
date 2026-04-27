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

url = "https://api.worldbank.org/v2/country/all/indicator/NY.GDP.MKTP.CD?format=json&per_page=20000"

data = get_data(url)
print(data.sample(20))
