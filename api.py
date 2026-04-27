import requests
import pandas as pd
import numpy as np


def api_call(url:str):
    response = requests.api.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        raise ValueError("API call failed, check URL is correct and working")
    
url = "https://data360api.worldbank.org/data360/data?DATABASE_ID=WB_WDI&INDICATOR=WB_WDI_SP_POP_TOTL&skip=0"
data = api_call(url)
print(data)