from utils import prepare_data, make_prediction
from pydantic_models import PredictRequest

def predict(request: PredictRequest):
    data = prepare_data(request)
    return make_prediction(data)


if __name__ == '__main__':
    req = PredictRequest(cylinders=6, 
                         weight=3093,
                         acceleration=15.0,
                         origin=1)
    
    print(predict(req))
    