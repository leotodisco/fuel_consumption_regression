from fastapi import FastAPI
from utils import prepare_data, make_prediction
from pydantic_models import PredictRequest, PredictionResponse

app = FastAPI()

@app.post("/predict", response_model=PredictionResponse)
def predict(request: PredictRequest):
    data = prepare_data(request)
    value=make_prediction(data)
    pred = PredictionResponse(value=float(value[0]))
    return pred

