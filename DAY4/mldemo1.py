import mlflow
import mlflow.sklearn
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import numpy as np

# Generate sample data
np.random.seed(42)
X = np.random.rand(100, 1) * 10
y = 3 * X.squeeze() + 7 + np.random.randn(100) * 2

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Start MLflow run
with mlflow.start_run():
    model = LinearRegression()
    model.fit(X_train, y_train)
    
    preds = model.predict(X_test)
    rmse = np.sqrt(mean_squared_error(y_test, preds))
    
    # Log model, parameters, metrics
    mlflow.log_param("model_type", "LinearRegression")
    mlflow.log_metric("rmse", rmse)
    
    # Save model
    mlflow.sklearn.log_model(model, "model")
    
    print(f"Model trained and logged with RMSE = {rmse:.2f}")
    print("Run ID:", mlflow.active_run().info.run_id)
