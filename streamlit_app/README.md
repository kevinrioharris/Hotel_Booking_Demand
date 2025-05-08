# Streamlit App – Hotel Booking Cancellation Prediction

This folder contains the code for the **Streamlit web application** that allows users to interactively explore hotel booking data and predict whether a booking will be **canceled** or **not canceled**.

---

## 🔧 Features

The app includes four main functionalities:

1. **Homepage**  
   - Welcome page with a brief project summary.

2. **Data Visualization**  
   - Interactive visual analysis of booking data using bar charts and histograms.

3. **Single Prediction**  
   - Users fill out a form to simulate a single booking.
   - The app returns whether the booking is likely to be **canceled** or **not canceled**.

4. **Batch Prediction**
   - **Manual input**: Add multiple records one by one and get predictions.
   - **CSV upload**: Upload a CSV file and receive batch predictions.

---

## 🧠 Model Info

The app uses a pre-trained **Random Forest Classifier** (stored in `model.pkl`) trained on hotel booking data. It predicts whether a booking will be **canceled (1)** or **not canceled (0)** based on user input.

