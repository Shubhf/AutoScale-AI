# app/model.py
import joblib

def predict(input_features):
    clf = joblib.load("model.joblib")
    return int(clf.predict([input_features])[0])
