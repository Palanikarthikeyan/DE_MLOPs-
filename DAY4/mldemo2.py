from flask import Flask, request, jsonify
import mlflow.sklearn
import numpy as np

app = Flask(__name__)

# Load model from MLflow
RUN_ID = "paste-your-run-id-here"
model = mlflow.sklearn.load_model(f"runs:/{RUN_ID}/model")

@app.route('/')
def home():
    return "Linear Regression MLflow + Flask API is running!"

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    X = np.array(data["X"]).reshape(-1, 1)
    preds = model.predict(X)
    return jsonify({"predictions": preds.tolist()})

if __name__ == '__main__':
    app.run(debug=True)
