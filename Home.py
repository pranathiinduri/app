import streamlit as st
import pandas as pd
from cleaning_data import final_df

def main():
    # Ensure 'PURCHASE_' column is in datetime format
    final_df['PURCHASE_'] = pd.to_datetime(final_df['PURCHASE_'], errors='coerce')

    # Sidebar Header
    st.header('Machine Learning Assignment')

    # Main Header
    st.title('Data Exploration and Sorting')

    # Create tabs for organization
    tab1, tab2 = st.tabs(["Data Overview", "Sorting Options"])

    # Tab 1: Data Overview
    with tab1:
        st.subheader("Data Overview")
        st.markdown(
            """
            Explore the raw data to get an understanding of its structure and content.
            Use the interactive table below to filter, search, and analyze the dataset.
            """
        )
        st.dataframe(final_df)

    # Tab 2: Sorting Options
    with tab2:
        st.subheader("Sorting Options")
        st.markdown(
            """
            Choose a column below to sort the dataset in descending order.
            Use this feature to analyze specific patterns or trends in the data.
            """
        )

        # Use radio buttons for sorting
        options = ["HSHD_NUM", "BASKET_NUM", "DATE", "PRODUCT_NUM", "DEPARTMENT", "COMMODITY", "PURCHASE_"]
        selection = st.radio(label="Sort by:", options=options)

        # Sort and display the DataFrame based on selection
        if selection == "DATE" or selection == "PURCHASE_":
            sorted_df = final_df.sort_values(by='PURCHASE_', ascending=False)
            st.info("Sorted by latest transaction details.")
        else:
            sorted_df = final_df.sort_values(by=selection, ascending=False)

        st.write(f"Displaying data sorted by **{selection}**:")
        st.dataframe(sorted_df)

