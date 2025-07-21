# app/main.py
from fastapi import FastAPI
from pydantic import BaseModel
import time
import psutil
from app.model import predict
from app.autoscaler import scale_resources

app = FastAPI()

class Input(BaseModel):
    features: list

@app.post("/predict/")
def get_prediction(data: Input):
    start = time.time()
    result = predict(data.features)
    latency = time.time() - start

    system_info = (psutil.cpu_percent(), psutil.virtual_memory().percent)
    scale_resources(latency, system_info)

    return {
        "prediction": result,
        "latency": round(latency, 4),
        "cpu": system_info[0],
        "memory": system_info[1]
    }
