# Hotel Booking Prediction

## Outline
- [Project Overview](#project-overview) 
- [Analytical Approach](#analytical-approach)
- [Modeling](#modelling)
- [Results](#results)
- [Tableau Dashboard](#tableau-dashboard)
- [Streamlit Application](#streamlit-application)
- [File Directory](#file-directory)

---

## Project Overview 

In the hospitality industry, online reservations have become the norm—providing convenience for guests and broader reach for hotels. However, this shift has led to a high volume of booking cancellations, which negatively impact hotel operations and revenue. Studies have shown:
- 19% of cancellations originate from hotel websites,
- 39% from Booking.com,
- 25% from Expedia over a four-month period.

### Why Do Guests Cancel?
- Guests often book multiple hotels and make a final decision closer to the arrival date.
- Free cancellation options promote low-commitment bookings.
- Unexpected events (e.g., weather, strikes, emergencies) can force last-minute cancellations.

### Problem Background & Stakeholders
Booking cancellations disrupt planning and profitability. Key stakeholders include:
- **Hotel Management**: Minimizing revenue loss.
- **Revenue Teams**: Need accurate forecasts for pricing and occupancy planning.
- **Marketing Teams**: Segment guests and reduce cancellations.
- **Strategy Teams**: Use insights to develop data-driven policies.

---

## Analytical Approach

### Evaluating Model Performance: False Positives vs. False Negatives

Understanding errors in prediction helps mitigate business risks:

#### False Positives (FP)
- **What it means**: The model predicts a cancellation, but the guest actually arrives.
- **Impact**: Unnecessary retention efforts (e.g., discounts or promotions).

#### False Negatives (FN)
- **What it means**: The model fails to predict a cancellation.
- **Impact**:
  - Empty rooms despite operational preparations.
  - Missed opportunities to rebook and recover revenue.

**Conclusion**: **False Negatives are more critical** due to direct revenue loss and planning inefficiencies.

### Evaluation Metrics

- **Recall**: Most important to capture as many actual cancellations as possible.
- **F2 Score**: Prioritizes recall over precision, useful when false negatives are more costly.

---

## Data Understanding

- **Dataset**: [Hotel Booking Demand – Kaggle](https://www.kaggle.com/datasets/jessemostipak/hotel-booking-demand/data)
- **Size**: 119,389 booking records
- **Target Variable**: `is_canceled`  
  - `1`: Booking was canceled  
  - `0`: Booking was honored

### Key Features

| Feature | Description |
|--------|-------------|
| `lead_time` | Days between booking and arrival |
| `adr` | Average Daily Rate |
| `hotel` | Hotel type: Resort or City |
| `customer_type` | Transient, Contract, Group, etc. |
| `is_repeated_guest` | Whether the guest is a return visitor |
| `previous_cancellations` | Number of past canceled bookings |
| `booking_changes` | Number of changes made to booking |
| `deposit_type` | No Deposit, Refundable, or Non-Refundable |
| ... | [`See project notebook for full list`](https://github.com/kevinrioharris/Hotel_Booking_Demand/blob/main/Hotel_Booking_Demand_Analysis.ipynb) |

---

## Modelling

We compared six classification algorithms with two undersampling methods:

### Algorithms:
- Logistic Regression
- K-Nearest Neighbors (KNN)
- Decision Tree
- Random Forest
- LightGBM
- XGBoost

### Resampling Methods:
- Random Undersampling
- SMOTE (Synthetic Minority Over-sampling Technique)

---

## Results

- **Best Model**: **Random Forest + Random Undersampling**
- **F2 Score**: **79%**
- **Recall**: **88%**
- **Top Feature**: `lead_time` – Guests with longer lead times are more likely to cancel.
- **Cost Impact**:
  - **Before ML**: $802,510
  - **After ML**: $267,150  
  → **Up to 60% cost reduction achieved using ML**

---

## Tableau Dashboard

🔗 [Hotel Booking Demand Dashboard](https://public.tableau.com/app/profile/kevin.rio.harristyando/viz/HotelBookingDemandAnalysis_17455173950900/GuestsSegmentation)

<img src="https://github.com/kevinrioharris/Hotel_Booking_Demand/blob/main/Tableau/Homepage.jpg" width="600"/>
<img src="https://github.com/kevinrioharris/Hotel_Booking_Demand/blob/main/Tableau/Guests%20Segmentation.jpg" width="600"/>
<img src="https://github.com/kevinrioharris/Hotel_Booking_Demand/blob/main/Tableau/Cancellation%20Analysis.jpg" width="600"/>
<img src="https://github.com/kevinrioharris/Hotel_Booking_Demand/blob/main/Tableau/Machine%20Learning%20Evaluation.jpg" width="600"/>

---

## Streamlit Application

🔗 **[Live App](https://gammateamdti.streamlit.app/)**

Features:
- Visual Exploratory Data Analysis
- Single Prediction Form
- Manual Input Batch Prediction
- CSV Upload for Batch Prediction

<img src="https://github.com/kevinrioharris/Hotel_Booking_Demand/blob/main/Streamlit%20Photos/Homepage.jpg" width="600"/>
<img src="https://github.com/kevinrioharris/Hotel_Booking_Demand/blob/main/Streamlit%20Photos/Data%20viz.png" width="600"/>
<img src="https://github.com/kevinrioharris/Hotel_Booking_Demand/blob/main/Streamlit%20Photos/Single%20Prediction.jpg" width="600"/>
<img src="https://github.com/kevinrioharris/Hotel_Booking_Demand/blob/main/Streamlit%20Photos/Manual%20Batch%20Prediction.jpg" width="600"/>
<img src="https://github.com/kevinrioharris/Hotel_Booking_Demand/blob/main/Streamlit%20Photos/Batch%20CSV%20Prediction.jpg" width="600"/>

---

## File Directory

- 📓 [`Hotel_Booking_Demand_Analysis.ipynb`](https://github.com/kevinrioharris/Hotel_Booking_Demand/blob/main/Hotel_Booking_Demand_Analysis.ipynb) — Main notebook with code, visualizations, and explanations.
- 📦 [`model.pkl`](https://github.com/kevinrioharris/Hotel_Booking_Demand/blob/main/model.pkl) — Trained ML model.
- 🧹 [`hotel_booking_cleaned.csv`](https://github.com/kevinrioharris/Hotel_Booking_Demand/blob/main/hotel_booking_cleaned.csv) — Cleaned dataset.
- 🌐 [`streamlit_app/`](https://github.com/kevinrioharris/Hotel_Booking_Demand/tree/main/streamlit_app) — Code for the Streamlit web application.  
  ➤ To run locally: ensure model file path is correct, then execute `Homepage.py` via terminal.

---

## Author
**Kevin Rio**  
🔗 [GitHub](https://github.com/kevinrioharris) | 🔗 [LinkedIn](https://www.linkedin.com/in/kevinrioharris)
