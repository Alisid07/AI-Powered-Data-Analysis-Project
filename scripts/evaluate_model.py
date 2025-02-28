import pandas as pd
from sklearn.metrics import classification_report
from joblib import load

def evaluate_model(model_name):
    df = pd.read_csv('data/processed_data.csv')
    X, y = df.iloc[:, :-1], df.iloc[:, -1]
    model = load(f'models/{model_name}.joblib')
    y_pred = model.predict(X)
    print(classification_report(y, y_pred))

if __name__ == '__main__':
    evaluate_model('random_forest')
