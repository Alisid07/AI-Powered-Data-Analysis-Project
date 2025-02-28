import pandas as pd
from sklearn.preprocessing import LabelEncoder

def preprocess_data(file_path):
    df = pd.read_csv(file_path)

    # Ensure dataset is not empty
    if df.empty:
        print("Error: The dataset is empty. Please check sample_data.csv.")
        return

    # Drop rows with missing values to prevent errors
    df.dropna(inplace=True)

    # Ensure at least one numeric column exists
    if df.select_dtypes(include=['number']).empty:
        print("Error: No numeric columns found in dataset.")
        return

    # Convert categorical columns using LabelEncoder
    for column in df.select_dtypes(include=['object']).columns:
        df[column] = LabelEncoder().fit_transform(df[column])

    # Ensure at least one target column exists
    if df.shape[1] < 2:
        print("Error: No target column found.")
        return

    # Save processed data
    df.to_csv('data/processed_data.csv', index=False)
    print('Data preprocessing complete.')

if __name__ == '__main__':
    preprocess_data('data/sample_data.csv')
