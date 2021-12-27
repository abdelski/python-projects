import os
import pandas as pd
from fastapi import FastAPI

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CACHE_DIR = os.path.join(BASE_DIR, 'cache')

data = os.path.join(CACHE_DIR, 'movies_dataset_refactored.csv')

app = FastAPI()

@app.get('/')
def read():
    return {'Hello': 'World!!!'}

@app.get('/movies')
def read_movies():
    df = pd.read_csv(data)
    return df.to_dict('Rank')
