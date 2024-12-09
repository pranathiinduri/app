import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
from cleaning_data import (
    seasonal_sales,
    seasonal_footfall,
    top_products_per_season,
    inventory_recommendation,
    brand_preference,
    organic_preference,
    merged_engagement_df,
    household_spend_trends
)

# Main Title
st.title("Retail Analytics Dashboard")

# Column Layout: Seasonal Trends on the Left, Demographics on the Right
col1, col2 = st.columns(2)

# Column 1: Seasonal Trends
with col1:
    st.subheader("Seasonal Trends")
    st.markdown("Analyze how sales, footfall, and top products vary across seasons.")

    # Plot: Total Sales by Season
    st.write("#### Total Sales by Season")
    fig1, ax1 = plt.subplots(figsize=(6, 4))
    sns.barplot(data=seasonal_sales, x='season', y='SPEND', ax=ax1, palette="Blues_d")
    ax1.set_title('Total Sales by Season')
    ax1.set_xlabel('Season')
    ax1.set_ylabel('Total Sales')
    st.pyplot(fig1)

    # Inventory Recommendations
    st.write("#### Inventory Recommendations")
    st.text(inventory_recommendation)

# Column 2: Demographics and Engagement
with col2:
    st.subheader("Demographics and Engagement")
    st.markdown("Explore spending patterns by household size, presence of children, and store location.")

    # Household Size vs Spend
    st.write("#### Impact of Household Size on Total Spend")
    boxplot_data = merged_engagement_df.groupby('HH_SIZE')['SPEND'].mean().reset_index()
    st.bar_chart(boxplot_data.set_index('HH_SIZE')['SPEND'])

    # Spending Trends Over Time
    st.write("#### Household Spending Trends Over Time")
    st.line_chart(household_spend_trends.set_index('YEAR')['SPEND'])

# Footer
st.markdown("---")
st.info("Use the filters and expanders in future iterations for deeper insights into your data.")
