# Fake Job Detection App

## Overview

This project is a Machine Learning-based web application that predicts whether a job posting is **Fake** or **Real**. It uses a Logistic Regression model trained on a labeled dataset of job listings. The app is deployed using **Streamlit**, providing a simple and interactive web interface for prediction.

## Dataset

The dataset used is `fake_job_postings.csv` which contains various job attributes such as:

* Job Description
* Employment Type
* Industry
* Telecommuting status
* Presence of Company Logo
* Screening Questions, etc.

## Models Trained

Two classification models were trained:

### 1. Logistic Regression

* **Training Accuracy**: 95.93%
* **Testing Accuracy**: 93.98%
* **Confusion Matrix**:

  ```
  [[3203  191]
   [  24  158]]
  ```
* **Classification Report**:

  ```
  Precision    Recall   F1-Score
  Class 0:     0.99       0.94       0.97
  Class 1:     0.45       0.87       0.60
  ```

### 2. Random Forest Classifier

* **Training Accuracy**: 99.99%
* **Testing Accuracy**: 97.84%
* **Confusion Matrix**:

  ```
  [[3394    0]
   [  77  105]]
  ```
* **Classification Report**:

  ```
  Precision    Recall   F1-Score
  Class 0:     0.98       1.00       0.99
  Class 1:     1.00       0.58       0.73
  ```

### Comparison:

Although Random Forest gives higher accuracy, **Logistic Regression detects more fake jobs** (higher recall for Class 1). Therefore, **Logistic Regression** is chosen for the final model.

## Final Model

The final model (`Logistic Regression`) is saved as a **pipeline** using `pickle` in the file:

```
fake_job_model.pkl
```

This model file is used by the Streamlit app for prediction.

---

## Streamlit Web Interface

### How to Run

1. Open the project folder in **PyCharm** or any code editor.
2. Open the terminal.
3. Run the app using:

   ```
   streamlit run App.py
   ```
4. If any library error occurs, install missing libraries using pip:

   ```
   pip install -r requirements.txt
   ```

---

## Streamlit Inputs

The app takes the following inputs:

* **Job Description** (Text Area)
* **Employment Type** (Dropdown)
* **Industry** (Dropdown)
* **Telecommuting** (0 or 1)
* **Has Company Logo** (0 or 1)
* **Has Screening Questions** (0 or 1)

Once the user clicks **Predict**, the model predicts whether the job is **Fake** or **Real**.

---

## Screenshots

### 1. Real Job Prediction

![Real Job Prediction](images/real_job_screenshot.png)

### 2. Fake Job Prediction

![Fake Job Prediction](images/fake_job_screenshot.png)

---

## Author

Developed by Muhammad Mahad

muhammadmahad.cs@gmail.com

