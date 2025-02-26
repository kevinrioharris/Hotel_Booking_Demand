import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Set up page configuration
st.set_page_config(page_title="Data Visualization", layout="wide", page_icon="📊")

st.title("Data Visualization for Hotel Booking Demand")
st.write("Explore data visualizations to gain insights into booking cancellations and key performance metrics.")
 
df = pd.read_csv(r".\hotel_booking_cleaned.csv")

# -----------------------------
# Booking Cancellation Distribution
# -----------------------------
st.header("Booking Cancellation Distribution")
fig, axs = plt.subplots(1, 2, figsize=(12, 8))
plt.subplots_adjust(left=0.05, right=0.95, top=0.85, bottom=0.15, wspace=0.3)
colors = ['#2ecc71', '#e74c3c']

# Pie Chart
axs[0].pie(
    df['is_canceled'].value_counts(),
    autopct='%.2f%%',
    labels=['Not Cancelled', 'Cancelled'],
    colors=colors,
    startangle=140,
    wedgeprops={'edgecolor': 'black'},
    textprops={'fontsize': 12, 'fontweight': 'semibold', 'color': 'white'}
)
axs[0].set_title('Booking Status', fontsize=14, fontweight='bold')

# Bar Chart
ax_bar = sns.countplot(data=df, x='is_canceled', hue='is_canceled', palette=colors, ax=axs[1])
for container in ax_bar.containers:
    ax_bar.bar_label(container, fmt='%d', padding=3, fontsize=12, fontweight='semibold')
ax_bar.set_xticks([0, 1])
ax_bar.set_xticklabels(['Not Cancelled', 'Cancelled'])
ax_bar.set_xlabel('')
ax_bar.set_ylabel('Count')
ax_bar.set_title('Count of Booking Status', fontsize=14, fontweight='bold')
ax_bar.legend(['Not Cancelled', 'Cancelled'])
ax_bar.grid(axis='y', linestyle='--', alpha=0.7)
st.pyplot(fig)

# -----------------------------
# Monthly Bookings Distribution
# -----------------------------
st.header("Monthly Bookings Distribution")
fig2, ax2 = plt.subplots(figsize=(12, 6))
df['arrival_date_month'].value_counts().plot(kind='bar', color='#2ecc71', ax=ax2)
ax2.set_title("Number of Bookings per Month", fontsize=14, fontweight='bold')
ax2.set_xlabel("Month")
ax2.set_ylabel("Number of Bookings")
ax2.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
st.pyplot(fig2)

# -----------------------------
# Cancellation Proportion: City vs. Resort Hotels
# -----------------------------
st.header("Cancellation Proportion: City vs. Resort Hotels")
fig3, ax3 = plt.subplots(figsize=(15, 10))
cancellation_data = pd.crosstab(df['hotel'], df['is_canceled'], normalize=0) * 100
ax3 = cancellation_data.plot(kind='bar', stacked=True, color=['#2ecc71', '#e74c3c'], edgecolor='black', ax=ax3)
for bars in ax3.containers:
    ax3.bar_label(bars, fmt='%.1f%%', label_type='center', color='white', weight='semibold')
ax3.legend(title='Cancellation', labels=['Not Canceled', 'Canceled'])
ax3.set_title('Cancellation Proportion: City vs. Resort Hotels', fontweight='bold')
ax3.set_xlabel('Hotel Type')
ax3.set_ylabel('Proportion')
ax3.set_xticklabels(ax3.get_xticklabels(), rotation=0)
ax3.grid(axis='y', linestyle='--', alpha=0.7)
st.pyplot(fig3)

# -----------------------------
# Cancellation Proportion between Market Segments
# -----------------------------
st.header("Cancellation Proportion: Market Segments")
fig4 = plt.figure(figsize=(20,8))
cancellation_data = pd.crosstab(df['market_segment'], df['is_canceled'], normalize=0) * 100
ax4 = cancellation_data.plot(
    kind='bar', 
    stacked=True, 
    color=['#2ecc71', '#e74c3c'], 
    edgecolor='black', 
    legend=False,
    ax=plt.gca()
)
for container in ax4.containers:
    ax4.bar_label(container, fmt="%.f%%", label_type='center', color='white', fontweight='semibold')
ax4.legend(title='Cancellation', labels=['Not Canceled', 'Canceled'])
ax4.set_title('Comparison of Cancellation Proportion between Market Segments', fontweight='bold')
ax4.set_xlabel('Market Segment')
ax4.set_ylabel('Proportion')
ax4.set_xticklabels(ax4.get_xticklabels(), rotation=0)
ax4.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
st.pyplot(fig4)

# -----------------------------
# Cancellation Proportion between Deposit Types
# -----------------------------
st.header("Cancellation Proportion: Deposit Types")
fig5 = plt.figure(figsize=(15,8))
deposit_cancel = pd.crosstab(df['deposit_type'], df['is_canceled'], normalize=0) * 100
ax5 = deposit_cancel.plot(
    kind='bar', 
    stacked=True, 
    color=['#2ecc71', '#e74c3c'], 
    edgecolor='black', 
    legend=False,
    ax=plt.gca()
)
for container in ax5.containers:
    ax5.bar_label(container, fmt="%.f%%", label_type='center', color='white', fontweight='semibold')

raw_counts = pd.crosstab(df['deposit_type'], df['is_canceled'])

for idx, deposit in enumerate(raw_counts.index):
    total_val = raw_counts.loc[deposit].sum()
    ax5.text(idx, 102, f"Total: {total_val}", ha="center", fontsize=10, fontweight="regular", color="black")

ax5.legend(title='Cancellation', labels=['Not Canceled', 'Canceled'])
ax5.set_title('Comparison of Cancellation Proportion between Deposit Types', fontweight='bold')
ax5.set_xlabel('Deposit Type')
ax5.set_ylabel('Proportion')
ax5.set_xticklabels(ax5.get_xticklabels(), rotation=0)
ax5.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
st.pyplot(fig5)

# -----------------------------
# Correlation Matrix
# -----------------------------
st.header("Correlation Matrix")
fig6, ax6 = plt.subplots(figsize=(16, 8))
num_corr = df.select_dtypes('number').drop(columns=['is_canceled']).corr()
matrix = np.triu(num_corr)
sns.heatmap(num_corr, annot=True, mask=matrix, cmap="coolwarm", ax=ax6)
ax4.set_title("Correlation Matrix", fontsize=14, fontweight='bold')
st.pyplot(fig6)