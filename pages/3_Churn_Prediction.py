import streamlit as st
import seaborn as sns
import pandas as pd
from cleaning_data import correlation_matrix, customer_engagement

# Tabs for better organization
tab1, tab2, tab3 = st.tabs(["Correlation Analysis", "Total Spend Trends", "Purchase Frequency Trends"])

# Tab 1: Correlation Analysis
with tab1:
    st.subheader("Correlation Analysis Between Disengagement and Demographics")
    st.markdown(
        """
        This chart showcases the correlation between various demographic features and disengagement.
        Darker shades indicate stronger positive or negative correlations.
        """
    )
    # Displaying heatmap using Streamlit's st.heatmap (if available)
    st.write("### Correlation Matrix")
    st.dataframe(correlation_matrix)  # Display the correlation matrix as a table for better interaction
    
    # Alternatively, if Streamlit's heatmap were available, you could use st.heatmap
    # For now, display the correlation matrix as a dataframe
    st.markdown("The following table shows the correlation between various demographic features and disengagement:")
    st.dataframe(correlation_matrix)

# Tab 2: Total Spend Trends
with tab2:
    st.subheader("Total Spend Trends by Disengagement Status")
    st.markdown(
        """
        Analyze the total spending trends over the years based on customer disengagement status.
        Use this chart to identify how disengaged customers' spending patterns differ from engaged customers.
        """
    )
    # Grouping and plotting the data using Streamlit's line_chart
    total_spend_trends = customer_engagement.groupby(['year', 'disengaged'])['total_spend'].sum().unstack()
    st.write("### Total Spend Over the Years by Disengagement Status")
    st.line_chart(total_spend_trends)

# Tab 3: Purchase Frequency Trends
with tab3:
    st.subheader("Purchase Frequency Trends by Disengagement Status")
    st.markdown(
        """
        This chart highlights how frequently purchases are made by engaged and disengaged customers over the years.
        Use it to observe shifts in engagement levels and their impact on purchase frequency.
        """
    )
    # Grouping and plotting the data using Streamlit's line_chart
    purchase_frequency_trends = customer_engagement.groupby(['year', 'disengaged'])['frequency_of_purchase'].sum().unstack()
    st.write("### Purchase Frequency Over the Years by Disengagement Status")
    st.line_chart(purchase_frequency_trends)
