# 🧬 Nadi Pulse Diabetes Predictor
A Streamlit-based web application that uses optical sensor pulse data to predict diabetes using a trained machine learning model.
This project processes nadi pulse data collected from an optical sensor and predicts diabetes using statistical features extracted from the pulse signals (3 channels). The app is built using Streamlit, and the model is trained using scikit-learn.

![Screenshot (37)](https://github.com/user-attachments/assets/9a4fe3c3-efbd-4aca-87b6-d0e7532c5199)
![Screenshot (38)](https://github.com/user-attachments/assets/fa11bec1-6f94-4e6a-824d-cbf8f7fde94c)
![Screenshot (39)](https://github.com/user-attachments/assets/6dace517-1519-4a1c-96ac-6f927724c682)
![Screenshot (40)](https://github.com/user-attachments/assets/9ed672b9-7baa-48cf-bd07-83e9fb07295c)

# 🧠 Features Used for Prediction
Channel 1, 2, 3 statistics:

Mean, Standard Deviation, Min, Max, Skewness

User Input:

Age

# 🧪 Prediction Output
✅ Healthy (Diabetes under control)

🤒 Diabetes - Not Controlled

🤒 Other Diseases like Anemia
# 📂 Sample Input Format (nadi_data.txt)
```sh
Start nPULSE001
2394,874,1492
2084,1021,1407
1500,1034,1901
2394,874,1492
2084,1021,1407
1500,1034,1901
...
       ```sh
# 🖥️ Running Locally
1. Clone the repository
```sh
   git clone https://github.com/AbuZar-Ansarii/Nadi-Diabetes.git
   cd nadi-diabetes-predictor
3. Install dependencies
  ```sh
   pip install -r requirements.txt
   
# 🐳 Running with Docker

   docker build -t abuzar718/nadi .

   docker run -p 8501:8501 abuzar718/nadi.
   







