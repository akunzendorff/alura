from fastapi import FastAPI

app = FastAPI()

@app.get('/api/hello')
def hello_world():
    return {'Hello': 'World'}