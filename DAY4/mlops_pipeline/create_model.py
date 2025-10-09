import mlflow
from sklearn.ensemble import RandomForestClassifier
import pandas as pd

def train_model():
    mlflow.set_tracking_uri('http://localhost:5000')
    model = RandomForestClassifier(n_estimators=10)
    x = pd.read_csv('data.csv')
    y = pd.read_csv('target.csv').values.ravel() # convert to 1D array
    model.fit(x,y)
    with mlflow.start_run(): # we log this model in mlflow
        mlflow.log_param('n_estimators',100)
        mlflow.sklearn.log_model(model,'Random Forest')
