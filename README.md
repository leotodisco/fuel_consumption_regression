# Polynomial Regression on MPG Dataset

This project is my **Polynomial Regression** project at the end of **Week 2, Course 1** of the **Andrew Ng Machine Learning Specialization**. It predicts vehicle fuel efficiency (MPG) based on several features in the dataset.

---

## Project Structure

The project is organized into several directories, each serving a specific purpose:

- **notebooks/**: This folder contains Jupyter notebooks for the full workflow. It includes notebooks for data collection, exploratory data analysis, data preparation, model experiments, and evaluation. These notebooks document the step-by-step process of building and analyzing the polynomial regression model.

- **src/**: The source code for the project is organized here.
  
- **data/**: This folder holds the dataset files. The raw dataset is stored here, as well as any cleaned and preprocessed versions used for training the model.

- **models/**: Pickled pipelines and models are saved in this folder. It includes the `data_pipeline.pkl` for preprocessing and the `polynomial_regression_pipeline.pkl` which contains the full pipeline including polynomial feature transformation and regression.

- **Dockerfile**: Contains instructions to build a Docker container for the project, making it easy to deploy the API in a reproducible environment.
  
---

## Dataset

The project uses the **Auto MPG dataset** from the [UCI Machine Learning Repository](https://archive.ics.uci.edu/dataset/9/auto+mpg). This dataset contains information about various car attributes and their corresponding miles per gallon (MPG) values. The goal is to predict the MPG based on the other features.

---

## Model

- **Type**: Polynomial Regression  
- **Pipeline**: Includes data preprocessing and polynomial feature transformation  
- **Metric**: RMSE (Root Mean Squared Error)  

---

## Notebooks

- **data_collection.ipynb** → Data collection  
- **eda.ipynb** → Exploratory Data Analysis  
- **data_preparation.ipynb** → Data cleaning and preprocessing  
- **experiments.ipynb** → Model training and experiments  
- **evaluation.ipynb** → Performance evaluation  

---

## API

The project includes a FastAPI service to make predictions with the trained model.

### Docker Commands

Build the image:

```bash
docker build -t fuel-regression-api .