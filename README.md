# Hotel Booking Prediction

Contributors:
- Kevin Rio Harristyando
- Theresia Diah Kusumaningrum
- Sekar Saraswati Wibowo

## Outline
- [Hotel Booking Cancellation Prediction](#Project-Overview) 
- [Tableau Dashboard](#Tableau-Dashboard)
- [Streamlit Application](#Streamlit-Application)
- [File Directory](#File-Directory)

## Project Overview 

In the hospitality industry, web reservations are the trend, offering convenience to travelers and expanded reach to hotels. All the same, with this shift has come a significant wave of booking cancellations that is proving difficult to hotel operations and revenue management. Studies have reported 19% of cancellations coming from a hotel's website, 39% from Booking.com, and 25% from Expedia in the course of a four-month period. (sources)

Several factors contribute to this large number of cancellations:

- Guests prefer booking multiple hotels simultaneously, planning to finalize a decision closer to the date of arrival. This practice makes it more likely to have cancellations as travelers limit their options.(sources)

- Free cancellation as an option encourages guests to reserve rooms with no strings attached, making cancellations more likely.

- Unforeseen situations such as bad weather, strikes, computer failures, or personal emergencies might disrupt travel schedules, leading to last-minute cancellations.

### Problem Background & Stakeholders
The hotel industry faces significant challenges related to booking cancellations, which can impact revenue, operational efficiency, and overall customer satisfaction. Key stakeholders include:

- **Hotel Management:** Seeks to minimize revenue loss due to last-minute cancellations.
- **Revenue Management Teams:** Need accurate cancellation predictions to implement dynamic pricing and optimize room allocation.
- **Marketing Departments:** Can target customers more effectively by understanding cancellation patterns.
- **Business Strategy Teams:** Focus on evaluating campaign effectiveness, measuring ROI, and developing actionable strategies for growth.

## Analytical Approach

### Evaluating Model Performance: Understanding False Positives and False Negatives

When predicting hotel booking cancellations, it is crucial to understand the implications of false positives and false negatives, as they directly impact revenue management and operational planning.

#### False Positives (FP)
- **Definition:**  
  The model predicts that a booking will be canceled, but in reality, it is not canceled.
- **Business Impact:**  
  - Wasted retention efforts (discounts or promotions given unnecessarily)

#### False Negatives (FN)
- **Definition:**  
  The model predicts that a booking will not be canceled, but in reality, it is canceled.
- **Business Impact:**  
  - **Lost Revenue:** When a cancellation is not predicted, the hotel may prepare for the guest's arrival (e.g., staffing, inventory, and service preparations) and incur associated costs, only to have the room remain vacant.
  - **Missed Rebooking Opportunities:** A false negative can prevent the hotel from proactively rebooking the room, leading to significant revenue loss.
  
### Deciding Which is More Critical: FP or FN?
- **False Negatives are more critical.**  
  In the context of hotel booking cancellation prediction, failing to identify a cancellation (FN) can lead to unoccupied rooms and lost revenue opportunities.

### Choosing Evaluation Metrics for Booking Cancellation Prediction
  
- **F2 Score:**  
  To find balance between recall and precision, with more emphasize on recall, using the F2 Score is essential. This metric helps in managing the trade-off between catching as many cancellations as possible (recall) while avoiding too many false alarms (precision) that can lead to unnecessary overbooking strategies.

- **Recall:**  
  Recall is the most critical metric in this scenario. A high recall ensures that the model captures as many actual cancellations as possible, minimizing the risk of unanticipated vacant rooms.


### Data Understanding
- **Source:** [Hotel Booking Demand Dataset on Kaggle](https://www.kaggle.com/datasets/jessemostipak/hotel-booking-demand/data)
- **Description:**  
  This dataset contains 119,389 historical booking records from hotels, which include various features such as booking details, customer demographics, and booking statuses. Each row in the dataset represents a single booking record.

- **Target Variable**  
  For our classification task, the target variable is **`is_canceled`**, where:
  - `1` indicates that the booking was canceled.
  - `0` indicates that the booking was not canceled.

- **Feature Overview**
  Below is a table summarizing the key features in the dataset:

| **Feature**                         | **Description**                                                                                               |
|-------------------------------------|-----------------------------------------------------------------------------------------------------------|
| **adr**                             | Average Daily Rate per room (in hotel currency).                                                          |
| **adults**                          | Number of adults in the booking.                                                                          |
| **agent**                           | Travel agent ID handling the booking (can be null).                                                       |
| **arrival_date_day_of_month**       | Day of the month when the arrival is scheduled.                                                           |
| **arrival_date_month**              | Month of arrival (e.g., "January", "February").                                                           |
| **arrival_date_week_number**        | Week number of the arrival date.                                                                          |
| **arrival_date_year**               | Year of arrival.                                                                                          |
| **assigned_room_type**              | Code of the room type actually assigned.                                                                 |
| **babies**                          | Number of babies in the booking.                                                                          |
| **booking_changes**                 | Number of changes made to the booking.                                                                    |
| **children**                        | Number of children in the booking (can be null).                                                          |
| **company**                         | Company ID associated with the booking (can be null).                                                     |
| **country**                         | Country of origin of the customer (can be null).                                                          |
| **customer_type**                   | Type of customer ("Transient", "Contract", "Group", "Transient-Party").                                  |
| **days_in_waiting_list**            | Number of days the booking was on the waiting list before confirmation.                                   |
| **deposit_type**                    | Type of deposit required ("No Deposit", "Non Refundable", "Refundable").                                  |
| **distribution_channel**            | Booking distribution channel (e.g., "TA/TO", "Direct").                                                  |
| **hotel**                           | Type of hotel ("Resort Hotel" or "City Hotel").                                                            |
| **is_canceled**                     | Booking cancellation status (1 = canceled, 0 = not canceled).                                             |
| **is_repeated_guest**               | Indicates if the guest has stayed at the hotel before (1 = Yes, 0 = No).                                  |
| **lead_time**                       | Number of days between booking and arrival.                                                               |
| **market_segment**                  | Market segment category (e.g., "Direct", "Corporate", "Online TA").                                       |
| **meal**                            | Type of meal plan booked (e.g., "BB" for Bed & Breakfast).                                                |
| **previous_bookings_not_canceled**  | Number of previous bookings that were not canceled.                                                       |
| **previous_cancellations**          | Number of previous bookings that were canceled.                                                           |
| **required_car_parking_spaces**     | Number of car parking spaces requested by the customer.                                                  |
| **reserved_room_type**              | Code of the room type initially reserved.                                                                 |
| **reservation_status**              | Final reservation status ("Canceled", "Check-Out", "No-Show").                                            |
| **reservation_status_date**         | Date when the reservation status was last updated.                                                       |
| **stays_in_week_nights**            | Number of weekday nights (Monday-Friday) included in the booking.                                         |
| **stays_in_weekend_nights**         | Number of weekend nights (Saturday/Sunday) included in the booking.                                       |
| **total_of_special_requests**       | Total number of special requests made (e.g., extra bed, high floor).                                      |

### EDA

![cancelled](https://github.com/user-attachments/assets/39242033-5cef-4260-b613-1864353cd8d0)

### Modelling

We compared the results of 6 different classification algorithms and applied 2 undersampling methods to find the best model.
**Models**
- Logistic Regression
- KNN (K-Nearest Neighbors)
- Decision Tree
- Random Forest
- LightGBM (Light Gradient Boosting Machine)
- XGBoost (Extreme Gradient Boosting)

**Undersampling Methods**
- Random Undersampling
- SMOTE

### Result
- The best performing model is Random Forest with the Random Undersampling method, resulting in F2 score of 79% and Recall score of 88%.
- Based on the Feature Importance and SHAP result, the feature with the highest impact on cancellations is **Lead Time**. Guests with longer lead time are more prone to cancel their bookings.
- With machine learning, we can achieve total cost reductions of up to 60% 

    Total Cost **Before** ML    : $802,510

    Total Cost **After** ML: $267,150

## Tableau Dashboard
Link : https://public.tableau.com/app/profile/gamma.team/viz/HotelBookingFinal_17405748492750/HotelBooking?publish=yes

<img width="564" alt="image" src="https://github.com/user-attachments/assets/2393f404-a0cc-4076-9037-4a9285b721c6" />
<img width="566" alt="image" src="https://github.com/user-attachments/assets/267a852b-8e88-4916-bad5-cfb957370bb2" />

<img width="568" alt="image" src="https://github.com/user-attachments/assets/bceab4f8-4aaa-4e40-acf2-1c0b04fea4ce" />
<img width="562" alt="image" src="https://github.com/user-attachments/assets/0cefa87c-4260-449b-aa24-068e0c1367d0" />



## Streamlit Application
Link: https://gammateamdti.streamlit.app/
![Homepage](https://raw.githubusercontent.com/PurwadhikaDev/GammaGroup_DTI_02_FinalProject/main/Streamlit%20Photos/Homepage.jpg)
![Data Visualization](https://raw.githubusercontent.com/PurwadhikaDev/GammaGroup_DTI_02_FinalProject/main/Streamlit%20Photos/Data%20viz.png)

![Single Prediction](https://raw.githubusercontent.com/PurwadhikaDev/GammaGroup_DTI_02_FinalProject/main/Streamlit%20Photos/Single%20Prediction.jpg)

![Manual Batch Prediction](https://raw.githubusercontent.com/PurwadhikaDev/GammaGroup_DTI_02_FinalProject/main/Streamlit%20Photos/Manual%20Batch%20Prediction.jpg)

![Batch CSV Prediction](https://raw.githubusercontent.com/PurwadhikaDev/GammaGroup_DTI_02_FinalProject/main/Streamlit%20Photos/Batch%20CSV%20Prediction.jpg)

## File Directory
- [Project notebook](https://github.com/PurwadhikaDev/GammaGroup_DTI_02_FinalProject/blob/main/Final_Project_Gamma_Team_Hotel_Booking_Demand_2_0.ipynb) : consisting code , explanation and visualization detail about this project
- [Model file](https://github.com/PurwadhikaDev/GammaGroup_DTI_02_FinalProject/blob/main/model.pkl)
- [Data after cleaning](https://github.com/PurwadhikaDev/GammaGroup_DTI_02_FinalProject/blob/main/hotel_booking_cleaned.csv)
- [Streamlit Code](https://github.com/PurwadhikaDev/GammaGroup_DTI_02_FinalProject/blob/main/Homepage.py) and (https://github.com/PurwadhikaDev/GammaGroup_DTI_02_FinalProject/tree/main/pages). To run streamlit from your computer you need to check file directory of the model. then run Homepage.py from terminal
