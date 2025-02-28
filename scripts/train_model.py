import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from joblib import dump

def train_model(model_name):
    # Load preprocessed data
    df = pd.read_csv('data/processed_data.csv')

    # Ensure dataset is not empty
    if df.empty:
        print("Error: The dataset is empty. Run data_preprocessing.py again.")
        return

    # Separate features and target variable
    X = df.iloc[:, :-1]
    y = df.iloc[:, -1]

    # Ensure X and y are not empty
    if X.empty or y.empty:
        print("Error: Features (X) or target (y) are empty. Check your dataset.")
        return

    # Split dataset into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train the model
    model = RandomForestClassifier()
    model.fit(X_train, y_train)

    # Save the trained model
    dump(model, f'models/{model_name}.joblib')

    print(f"Model {model_name} trained and saved.")

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--model', required=True, choices=['random_forest'])
    args = parser.parse_args()
    train_model(args.model)
