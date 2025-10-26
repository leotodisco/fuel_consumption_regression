from pydantic import BaseModel


class PredictionResponse(BaseModel):
    value: float


class PredictRequest(BaseModel):
    cylinders: int
    weight: int
    acceleration: float
    origin: int
