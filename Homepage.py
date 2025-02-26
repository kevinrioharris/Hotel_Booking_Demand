import streamlit as st

st.set_page_config(
    page_title="Hotel Booking Demand Analysis and Prediction",
    layout="wide",
    page_icon="🏨"
)

st.title("Hotel Booking Demand Analysis and Prediction")
st.write("Welcome to the analytical dashboard for hotel booking demand and cancellation prediction.")
st.write("Use the sidebar to navigate between pages.")


st.header("Problem Background & Stakeholders")
st.write("""
The hotel industry faces significant challenges related to booking cancellations, which can impact revenue, operational efficiency, and overall customer satisfaction. Key stakeholders include:
- **Hotel Management:** Seeks to minimize revenue loss due to last-minute cancellations.
- **Revenue Management Teams:** Need accurate cancellation predictions to implement dynamic pricing and optimize room allocation.
- **Marketing Departments:** Can target customers more effectively by understanding cancellation patterns.
- **Business Strategy Teams:** Focus on evaluating campaign effectiveness, measuring ROI, and developing actionable strategies for growth.
""")

st.header("Context")
st.write("""
In the hospitality industry, web reservations are the trend, offering convenience to travelers and expanded reach to hotels. However, this shift has led to a significant wave of booking cancellations that challenges hotel operations and revenue management. Studies have reported that 19% of cancellations come from a hotel's website, 39% from Booking.com, and 25% from Expedia over a four-month period.

Several factors contribute to these high cancellation rates:
- **Multiple Bookings:** Guests often reserve rooms at multiple hotels and finalize their decision closer to the arrival date, which increases the likelihood of cancellations.
- **Free Cancellation Policies:** The availability of free cancellation encourages guests to book without long-term commitment, leading to higher cancellation rates.
- **Unforeseen Events:** Situations such as bad weather, strikes, technical failures, or personal emergencies can disrupt travel plans, resulting in last-minute cancellations.
""")

st.header("Dashboard Overview")
st.write("""
This dashboard provides interactive tools and clear visualizations that help you:
- **Predict Booking Cancellations:** Quickly identify which bookings are at high risk of cancellation.
- **Understand Key Influencers:** See how factors such as pricing, customer behavior, and booking modifications affect cancellation rates, so we can make better-informed decisions.
""")

st.markdown("""
---
**Developed by Gamma Team:**

- **Kevin Rio Harristyando**
- **Theresia Diah Kusumaningrum**
- **Sekar Saraswati Wibowo**
""")
