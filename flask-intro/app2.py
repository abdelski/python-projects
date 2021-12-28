from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def hello_world():
    return {'hello': 'world from FastAPI'}

@app.get('/data')
def get_data():
    return {'data': [1,2,3]}
