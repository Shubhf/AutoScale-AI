# train_model.py
from sklearn.datasets import load_digits
from sklearn.ensemble import RandomForestClassifier
import joblib

def train_model():
    X, y = load_digits(return_X_y=True)
    clf = RandomForestClassifier(n_estimators=10)
    clf.fit(X, y)
    joblib.dump(clf, "model.joblib")
    print("Model trained and saved as model.joblib")

if __name__ == "__main__":
    train_model()
