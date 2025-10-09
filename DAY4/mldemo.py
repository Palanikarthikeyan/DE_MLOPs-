import mlflow
import mlflow.sklearn
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

import pandas as pd
import numpy as np
'''
## data
np.random.seed(40)
X = np.random.rand(100,1) * 10 # features
Y = 3 * X.squeeze()+ 7 + np.random.randn(100)*2 # target value

X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.2,random_state=42)

with mlflow.start_run():
    model = LinearRegression()
    model.fit(X_train,Y_train)
    Y_pred = model.predict(X_test)
    mlflow.log_param("model_type","LinearReg")
    mlflow.log_metric("predict_value",Y_pred)
    print("model and metrics are updated")
'''
data = {'Hrs':[1,1.5,2.5,3.0,3.5],'Score':[30,44,55,70,80]}

df = pd.DataFrame(data)

X = df[['Hrs']] # independent 
Y = df[['Score']] # dependent
with mlflow.start_run():
    model = LinearRegression()
    model.fit(X,Y)
    mlflow.log_param('model_type','LinearReg')
    mlflow.log_metric('predict value',0.9)



