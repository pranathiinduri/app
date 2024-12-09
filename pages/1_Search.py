import streamlit as st
from cleaning_data import final_df
import pandas as pd

# Ensure the `PURCHASE_` column is in the correct format for sorting
final_df['PURCHASE_'] = pd.to_datetime(final_df['PURCHASE_'], errors='coerce')

# Sidebar Section for Filters and Sorting
st.sidebar.header("Filter and Sort Options")

# Filter by HSHD_NUM
hshd_num_search = st.sidebar.text_input("Search by HSHD_NUM:", placeholder="Enter HSHD_NUM")

# Apply filter
if hshd_num_search:
    filtered_df = final_df[final_df['HSHD_NUM'].astype(str).str.contains(hshd_num_search)]
else:
    filtered_df = final_df

# Sorting options
sort_by = st.sidebar.selectbox(
    "Sort by column:",
    options=["HSHD_NUM", "BASKET_NUM", "PURCHASE_", "PRODUCT_NUM", "DEPARTMENT", "COMMODITY"],
    index=0
)
sort_order = st.sidebar.radio("Sort Order:", options=["Ascending", "Descending"], index=0)

# Sorting logic
is_descending = sort_order == "Descending"
sorted_df = filtered_df.sort_values(by=sort_by, ascending=not is_descending)

# Main Content with Tabs
st.title("Data Analysis Dashboard")
tab1, tab2 = st.tabs(["📊 Data Table", "📈 Summary Statistics"])

# Tab 1: Display Filtered and Sorted Data
with tab1:
    st.subheader("Filtered and Sorted Data")
    st.write(f"Showing results filtered by `HSHD_NUM`: **{hshd_num_search or 'All'}**, sorted by `{sort_by}` in **{sort_order}** order.")
    st.dataframe(sorted_df, use_container_width=True)

# Tab 2: Summary Statistics
with tab2:
    st.subheader("Summary Statistics")
    st.markdown(
        """
        View key statistics for the displayed data, including count, mean, and standard deviation for numeric columns.
        """
    )
    if not sorted_df.empty:
        st.write(sorted_df.describe())
    else:
        st.info("No data available to display statistics. Adjust your filters.")

# Footer Section
st.sidebar.markdown("---")
st.sidebar.write("**Quick Tips**")
st.sidebar.info("Use the sidebar options to filter and sort the dataset dynamically.")
