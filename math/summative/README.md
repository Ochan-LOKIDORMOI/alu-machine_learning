**Students Performance Prediction Model and App**


Welcome to the Students Performance Prediction Model and App repository. This repository contains three main components: a machine learning model that predicts students' performance index based on input features, a Flutter app that interacts with the model to provide performance predictions, and a folder for the Colab Notebook on Univariate regression. This README file will guide you through the structure, setup, and usage of these components.

**Overview**

This project aims to predict a student's performance index based on several input features, including hours studied, previous scores, sleep hours, and the number of sample question papers practiced.

**Porject Structure**
.
├── API/
│   ├── main.py
│   ├── model.pkl
│   ├── requirements.txt
└── flutterApp/
    ├── lib/
    │   └── main.dart
    ├── pubspec.yaml
└── linear_regression/
    ├── Students_Performance_Index_multivariate.ipynb
    ├── Summative_Assignment_Ochan_LOKIDORMOI.ipynb


**API Endpoint**
The API is hosted publicly and can be accessed to get predictions by providing the necessary input values.

Public API Endpoint
POST https://alu-machine-learning-lfkq.onrender.com/predict live on render

**Request Format**
The API expects a JSON object with the following fields:
{
    "hours_studied": 7,
    "previous_scores": 99,
    "sleep_hours": 9,
    "sample_question_papers_practiced": 1
}

**Response Format**
The API returns a JSON object with the predicted performance index:
{
    "performance_index": 91.0
}

**Example Request using Postman**
- Open Postman.
- Create a new POST request.
- Set the URL to https://alu-machine-learning-lfkq.onrender.com/predict. which is live on render

**Enter the following JSON data:**
In the body of the request, select raw and JSON format.
{
    "hours_studied": 7,
    "previous_scores": 99,
    "sleep_hours": 9,
    "sample_question_papers_practiced": 1
}

Send the request and you will receive the predicted performance index in the response.

**Flutter Application**
A simple Flutter application is provided to interact with the API.

- Flutter Application Setup
- Navigate to the flutter_app directory.
- Ensure you have Flutter installed. If not, follow the instructions at https://flutter.dev/.
- Run the following command to install the dependencie

- flutter pub get
- flutter run

**App Features**
- Input fields to enter hours studied, previous scores, sleep hours, and the number of sample question papers practiced.
- A button to get the predicted performance index.
- Display the prediction result.




