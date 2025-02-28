# 🚀 AI-Powered Data Analysis Project

This project applies **machine learning** techniques to analyze datasets and make predictions. It includes **data preprocessing, exploratory data analysis (EDA), model training, evaluation, and API deployment** using FastAPI.

## 📌 Features
- ✅ **Data Preprocessing**: Handles missing values & encodes categorical data.
- 📊 **Exploratory Data Analysis (EDA)**: Generates data visualizations.
- 🎯 **Model Training**: Uses a **Random Forest classifier**.
- 📈 **Model Evaluation**: Computes accuracy & classification metrics.
- 🌍 **API Deployment**: Allows predictions via **FastAPI**.

---

## 📂 Project Structure
AI-Powered-Data-Analysis-Project/ ├── app/ # FastAPI backend │ ├── main.py # API for model predictions ├── data/ # Raw & processed data │ ├── sample_data.csv # Input dataset │ ├── processed_data.csv # Preprocessed data ├── models/ # Trained models │ ├── random_forest.joblib ├── scripts/ # Data processing & model training │ ├── data_preprocessing.py │ ├── eda.py │ ├── train_model.py │ ├── evaluate_model.py ├── README.md # Project documentation ├── requirements.txt # Python dependencies └── .gitignore # Ignore unnecessary files

yaml
Copy
Edit

---

## 🔧 Installation & Usage
**1️⃣ Clone the Repository**
```bash
git clone https://github.com/yourusername/AI-Powered-Data-Analysis-Project.git
cd AI-Powered-Data-Analysis-Project
2️⃣ Install Dependencies

bash
Copy
Edit
pip install -r requirements.txt
3️⃣ Run Data Preprocessing

bash
Copy
Edit
python scripts/data_preprocessing.py
4️⃣ Train the Model

bash
Copy
Edit
python scripts/train_model.py --model random_forest
5️⃣ Evaluate the Model

bash
Copy
Edit
python scripts/evaluate_model.py
🌍 API Deployment
The project includes a FastAPI-based API for making predictions.

Run the API:

bash
Copy
Edit
uvicorn app.main:app --reload
Open your browser at http://127.0.0.1:8000/docs to test the API.
📊 Example Prediction
Make a POST request to /predict with JSON input:

json
Copy
Edit
{
    "Age": 30,
    "Salary": 60000,
    "Department": 2
}
Response:

json
Copy
Edit
{
    "prediction": 1
}
📜 License
This project is licensed under the MIT License.

🤝 Contributing
Contributions are welcome! Feel free to fork this repo and submit a pull request.

⭐ Show Your Support
If you like this project, please star this repository! 🌟
