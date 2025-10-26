import joblib
import pandas as pd
from pydantic_models import PredictRequest

data_pipeline = joblib.load("models/data_cleaning_pipeline.pkl")
regression_pipeline = joblib.load("models/polynomial_regression.pkl")
continuous_features = ["weight", "acceleration"]
ordinal_features = ["cylinders"]
nominal_features = ["origin"]

def prepare_data(request: PredictRequest):
    dictionary = request.model_dump()
    dataframe_row = pd.DataFrame([dictionary])
    transformed = data_pipeline.transform(dataframe_row)
    
    ohe = data_pipeline.named_transformers_['nominal_pipe']
    ohe_columns = ohe.get_feature_names_out(nominal_features)
    column_names = ordinal_features + continuous_features + list(ohe_columns)
    transformed_df = pd.DataFrame(transformed, columns=column_names)

    transformed_df = transformed_df.rename(columns={"origin_1.0": "USA", "origin_2.0":"Europe", "origin_3.0":"Asia"})
    return transformed_df
    

def make_prediction(data):
    return regression_pipeline.predict(data)