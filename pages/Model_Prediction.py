import streamlit as st
import pandas as pd
import joblib
import numpy as np

st.set_page_config(
    page_title="Hotel Booking Cancellation Prediction",
    layout="wide",
    page_icon="🧠"
)

st.title("Hotel Booking Cancellation Prediction")
st.write("Predict whether a hotel booking will be canceled based on key booking details.")

model = joblib.load(r'.\model.pkl')

df = pd.read_csv(".\hotel_booking_cleaned.csv")

def get_unique(col):
    return sorted(df[col].fillna("Unknown").unique().tolist())

prediction_mode = st.radio("Select Prediction Mode", ("Single Prediction", "Batch Prediction (Manual)", "Batch Prediction (CSV)"))

# Single Prediction Mode
if prediction_mode == "Single Prediction":
    st.sidebar.subheader("Input Booking Details")
    
    # Numerical inputs
    lead_time = st.sidebar.slider("Lead Time (days)", min_value=0, max_value=365, value=50)
    adr = st.sidebar.number_input("Average Daily Rate (ADR)", min_value=0.0, value=100.0, step=1.0)
    booking_changes = st.sidebar.slider("Booking Changes", min_value=0, max_value=10, value=1)
    total_of_special_requests = st.sidebar.slider("Total Special Requests", min_value=0, max_value=5, value=0)
    previous_cancellations = st.sidebar.number_input("Previous Cancellations", min_value=0, max_value=20, value=0, step=1)
    previous_bookings_not_canceled = st.sidebar.number_input("Previous Bookings Not Canceled", min_value=0, max_value=20, value=0, step=1)
    days_in_waiting_list = st.sidebar.number_input("Days in Waiting List", min_value=0, max_value=50, value=0, step=1)
    arrival_date_day_of_month = st.sidebar.number_input("Arrival Date Day of Month", min_value=1, max_value=31, value=15, step=1)
    arrival_date_week_number = st.sidebar.number_input("Arrival Date Week Number", min_value=1, max_value=53, value=25, step=1)
    
    # Guest details
    adults = st.sidebar.slider("Number of Adults", min_value=1, max_value=10, value=2)
    children = st.sidebar.slider("Number of Children", min_value=0, max_value=10, value=0)
    babies = st.sidebar.slider("Number of Babies", min_value=0, max_value=10, value=0)
    total_guests = adults + children + babies
    is_family = True if (children > 0 or babies > 0) else False
    
    stays_in_week_nights = st.sidebar.slider("Week Nights Stay", min_value=0, max_value=14, value=2)
    stays_in_weekend_nights = st.sidebar.slider("Weekend Nights Stay", min_value=0, max_value=14, value=1)
    
    total_nights = stays_in_week_nights + stays_in_weekend_nights

    hotel_type = st.sidebar.selectbox("Hotel Type", get_unique("hotel"))
    arrival_date_month = st.sidebar.selectbox("Arrival Date Month", get_unique("arrival_date_month"))
    meal = st.sidebar.selectbox("Meal", get_unique("meal"))
    country = st.sidebar.selectbox("Country", get_unique("country"))
    market_segment = st.sidebar.selectbox("Market Segment", get_unique("market_segment"))
    distribution_channel = st.sidebar.selectbox("Distribution Channel", get_unique("distribution_channel"))
    is_repeated_guest = st.sidebar.selectbox("Repeated Guest", ("Yes", "No"))
    reserved_room_type = st.sidebar.selectbox("Reserved Room Type", get_unique("reserved_room_type"))
    deposit_type = st.sidebar.selectbox("Deposit Type", get_unique("deposit_type"))
    agent = st.sidebar.selectbox("Agent", get_unique("agent"))
    company = st.sidebar.selectbox("Company", get_unique("company"))
    customer_type = st.sidebar.selectbox("Customer Type", get_unique("customer_type"))
    
    display_data = {
        "hotel": hotel_type,
        "lead_time": lead_time,
        "arrival_date_month": arrival_date_month,
        "arrival_date_week_number": arrival_date_week_number,
        "arrival_date_day_of_month": arrival_date_day_of_month,
        "adults": adults,
        "children": children,
        "babies": babies,
        "meal": meal,
        "country": country,
        "market_segment": market_segment,
        "distribution_channel": distribution_channel,
        "is_repeated_guest": is_repeated_guest,
        "previous_cancellations": previous_cancellations,
        "previous_bookings_not_canceled": previous_bookings_not_canceled,
        "reserved_room_type": reserved_room_type,
        "booking_changes": booking_changes,
        "deposit_type": deposit_type,
        "agent": agent,
        "company": company,
        "days_in_waiting_list": days_in_waiting_list,
        "customer_type": customer_type,
        "adr": adr,
        "required_car_parking_spaces": st.sidebar.slider("Car Parking Spaces", min_value=0, max_value=10, value=0),
        "total_of_special_requests": total_of_special_requests,
        "stays_in_week_nights": stays_in_week_nights,
        "stays_in_weekend_nights": stays_in_weekend_nights
    }
    
    predict_data = {
        "hotel": hotel_type,
        "lead_time": lead_time,
        "arrival_date_month": arrival_date_month,
        "arrival_date_week_number": arrival_date_week_number,
        "arrival_date_day_of_month": arrival_date_day_of_month,
        "total_guests": total_guests,
        "is_family": is_family,
        "meal": meal,
        "country": country,
        "market_segment": market_segment,
        "distribution_channel": distribution_channel,
        "is_repeated_guest": 1 if is_repeated_guest == "Yes" else 0,
        "previous_cancellations": previous_cancellations,
        "previous_bookings_not_canceled": previous_bookings_not_canceled,
        "reserved_room_type": reserved_room_type,
        "booking_changes": booking_changes,
        "deposit_type": deposit_type,
        "agent": agent,
        "company": company,
        "days_in_waiting_list": days_in_waiting_list,
        "customer_type": customer_type,
        "adr": adr,
        "required_car_parking_spaces": display_data["required_car_parking_spaces"],
        "total_of_special_requests": total_of_special_requests,
        "total_nights": total_nights
    }
    
    st.subheader("Booking Details (Input)")
    st.table(pd.DataFrame([display_data]))
    
    if st.button("Predict Cancellation"):
        prediction = model.predict(pd.DataFrame([predict_data]))
        result = "Canceled" if prediction[0] == 1 else "Not Canceled"
        
        if result == "Canceled":
            st.markdown("<h2 style='color: red; text-align: center;'>🚨 Prediction: The booking is likely to be Canceled! 🚨</h2>", unsafe_allow_html=True)
        else:
            st.markdown("<h2 style='color: green; text-align: center;'>✅ Prediction: The booking is not likely to be Canceled ✅</h2>", unsafe_allow_html=True)

elif prediction_mode == "Batch Prediction (CSV)":
    st.subheader("Batch Prediction (CSV Upload)")
    uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])

    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        batch_df = df.copy()

        # Add derived columns
        batch_df["total_guests"] = batch_df["adults"] + batch_df["children"] + batch_df["babies"]
        batch_df["total_nights"] = batch_df["stays_in_week_nights"]+batch_df["stays_in_week_nights"]
        batch_df["is_family"] = batch_df.apply(lambda row: 1 if (row["children"] > 0 or row["babies"] > 0) else 0, axis=1)

        prediction_features = [
            "hotel", "lead_time", "arrival_date_month", "arrival_date_week_number",
            "arrival_date_day_of_month", "total_guests", "is_family", "meal", "country",
            "market_segment", "distribution_channel", "is_repeated_guest", "previous_cancellations",
            "previous_bookings_not_canceled", "reserved_room_type", "booking_changes",
            "deposit_type", "agent", "company", "days_in_waiting_list", "customer_type",
            "adr", "required_car_parking_spaces", "total_of_special_requests", "total_nights"
        ]

        batch_data = batch_df[prediction_features]

        if st.button("Predict Batch (CSV)"):
            predictions = model.predict(batch_df)
            df["prediction"] = predictions

            np.random.seed(42)
            df["random_guess"] = np.random.randint(0, 2, size=df.shape[0])

            st.markdown("### Prediction Results")
            st.dataframe(df)

            output_csv = df.to_csv(index=False).encode("utf-8")

            st.download_button(
                label="Download Predictions as CSV",
                data=output_csv,
                file_name="hotel_booking_predictions.csv",
                mime="text/csv"
            )   

else:  
    st.subheader("Batch Prediction (Manual Input)")
    num_rows = st.number_input("Number of Bookings to Input", min_value=1, max_value=100, step=1, value=1)
    manual_data_list = []
    
    st.markdown("## Enter Booking Details")
    for i in range(num_rows):
        with st.expander(f"Booking {i+1} Details", expanded=True):
            # Numerical inputs
            lead_time = st.number_input(f"Lead Time (days) (Booking {i+1})", min_value=0, max_value=365, value=50, key=f"b_lead_time_{i}")
            adr = st.number_input(f"Average Daily Rate (ADR) (Booking {i+1})", min_value=0.0, value=100.0, step=1.0, key=f"b_adr_{i}")
            booking_changes = st.number_input(f"Booking Changes (Booking {i+1})", min_value=0, max_value=10, value=1, key=f"b_booking_changes_{i}")
            total_of_special_requests = st.number_input(f"Total Special Requests (Booking {i+1})", min_value=0, max_value=5, value=0, key=f"b_special_requests_{i}")
            previous_cancellations = st.number_input(f"Previous Cancellations (Booking {i+1})", min_value=0, max_value=20, value=0, key=f"b_prev_cancellations_{i}")
            previous_bookings_not_canceled = st.number_input(f"Previous Bookings Not Canceled (Booking {i+1})", min_value=0, max_value=20, value=0, key=f"b_prev_not_cancellations_{i}")
            days_in_waiting_list = st.number_input(f"Days in Waiting List (Booking {i+1})", min_value=0, max_value=50, value=0, key=f"b_waiting_{i}")
            arrival_date_day_of_month = st.number_input(f"Arrival Date Day of Month (Booking {i+1})", min_value=1, max_value=31, value=15, key=f"b_arr_day_{i}")
            arrival_date_week_number = st.number_input(f"Arrival Date Week Number (Booking {i+1})", min_value=1, max_value=53, value=25, key=f"b_arr_week_{i}")
            
            # Guest details
            adults = st.number_input(f"Number of Adults (Booking {i+1})", min_value=1, max_value=10, value=2, key=f"b_adults_{i}")
            children = st.number_input(f"Number of Children (Booking {i+1})", min_value=0, max_value=10, value=0, key=f"b_children_{i}")
            babies = st.number_input(f"Number of Babies (Booking {i+1})", min_value=0, max_value=10, value=0, key=f"b_babies_{i}")
            total_guests = adults + children + babies
            
            # Night details
            stays_in_week_nights = st.number_input(f"Week Nights Stay (Booking {i+1})", min_value=0, max_value=14, value=2, key=f"b_week_nights_{i}")
            stays_in_weekend_nights = st.number_input(f"Weekend Nights Stay (Booking {i+1})", min_value=0, max_value=14, value=1, key=f"b_weekend_nights_{i}")
            total_nights = stays_in_week_nights + stays_in_weekend_nights
            
            # Compute is_family flag
            is_family = True if (children > 0 or babies > 0) else False
            
            # Categorical inputs
            hotel_type = st.selectbox(f"Hotel Type (Booking {i+1})", get_unique("hotel"), key=f"b_hotel_{i}")
            arrival_date_month_cat = st.selectbox(f"Arrival Date Month (Booking {i+1})", get_unique("arrival_date_month"), key=f"b_arr_month_{i}")
            meal = st.selectbox(f"Meal (Booking {i+1})", get_unique("meal"), key=f"b_meal_{i}")
            country = st.selectbox(f"Country (Booking {i+1})", get_unique("country"), key=f"b_country_{i}")
            market_segment = st.selectbox(f"Market Segment (Booking {i+1})", get_unique("market_segment"), key=f"b_market_{i}")
            distribution_channel = st.selectbox(f"Distribution Channel (Booking {i+1})", get_unique("distribution_channel"), key=f"b_dist_{i}")
            is_repeated_guest = st.selectbox(f"Repeated Guest (Booking {i+1})", ("Yes", "No"), key=f"b_repeat_{i}")
            reserved_room_type = st.selectbox(f"Reserved Room Type (Booking {i+1})", get_unique("reserved_room_type"), key=f"b_reserved_{i}")
            deposit_type = st.selectbox(f"Deposit Type (Booking {i+1})", get_unique("deposit_type"), key=f"b_deposit_{i}")
            agent = st.selectbox(f"Agent (Booking {i+1})", get_unique("agent"), key=f"b_agent_{i}")
            company = st.selectbox(f"Company (Booking {i+1})", get_unique("company"), key=f"b_company_{i}")
            customer_type = st.selectbox(f"Customer Type (Booking {i+1})", get_unique("customer_type"), key=f"b_cust_type_{i}")
            
            # Optionally, display raw guest and night details
            st.markdown("**Raw Guest & Night Details:**")
            st.table(pd.DataFrame({
                "Adults": [adults],
                "Children": [children],
                "Babies": [babies],
                "Week Nights": [stays_in_week_nights],
                "Weekend Nights": [stays_in_weekend_nights]
            }))
            
            booking_dict = {
                "hotel": hotel_type,
                "lead_time": lead_time,
                "arrival_date_month": arrival_date_month_cat,
                "arrival_date_week_number": arrival_date_week_number,
                "arrival_date_day_of_month": arrival_date_day_of_month,
                "total_guests": total_guests,
                "is_family": is_family,
                "meal": meal,
                "country": country,
                "market_segment": market_segment,
                "distribution_channel": distribution_channel,
                "is_repeated_guest": 1 if is_repeated_guest == "Yes" else 0,
                "previous_cancellations": previous_cancellations,
                "previous_bookings_not_canceled": previous_bookings_not_canceled,
                "reserved_room_type": reserved_room_type,
                "booking_changes": booking_changes,
                "deposit_type": deposit_type,
                "agent": agent,
                "company": company,
                "days_in_waiting_list": days_in_waiting_list,
                "customer_type": customer_type,
                "adr": adr,
                "required_car_parking_spaces": st.number_input(f"Car Parking Spaces (Booking {i+1})", min_value=0, max_value=10, value=0, key=f"b_parking_{i}"),
                "total_of_special_requests": total_of_special_requests,
                "total_nights": total_nights
            }
            
            manual_data_list.append(booking_dict)
    
    if manual_data_list:
        st.markdown("## Manual Batch Data for Prediction")
        manual_data_df = pd.DataFrame(manual_data_list)
        st.dataframe(manual_data_df)
        
        if st.button("Predict Batch (Manual)"):
            predictions = model.predict(manual_data_df)
            manual_data_df["Cancellation Prediction"] = ["Canceled" if pred == 1 else "Not Canceled" for pred in predictions]
            
            st.markdown("## Prediction Results")
            
            # Display individual alert messages for each booking
            for idx, row in manual_data_df.iterrows():
                if row["Cancellation Prediction"] == "Canceled":
                    st.error(f"Booking {idx+1}: Prediction: The booking is likely to be Canceled! 🚨")
                else:
                    st.success(f"Booking {idx+1}: Prediction: The booking is not likely to be Canceled. ✅")

