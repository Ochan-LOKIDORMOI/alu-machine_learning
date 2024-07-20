from fastapi import FastAPI
from pydantic import BaseModel
import numpy as np
import joblib

# Define the input data model
class InputData(BaseModel):
    hours_studied: float
    previous_scores: float
    sleep_hours: float
    sample_question_papers_practiced: int

# Load a pre-trained model (replace with your model path)
# Assume the model is saved as 'model.joblib'
model = joblib.load("model.pkl")

# Create the FastAPI app
app = FastAPI()

@app.post("/predict")
def predict(data: InputData):
    # Prepare the input data for prediction
    input_features = np.array([
        data.hours_studied,
        data.previous_scores,
        data.sleep_hours,
        data.sample_question_papers_practiced
    ]).reshape(1, -1)
    
    # Make a prediction
    prediction = model.predict(input_features)
    
    # Return the prediction
    return {"performance_index": prediction[0]}

# To run the app, use the command:
# uvicorn myapp:app --reload
# (Replace `myapp` with the filename of your script)
