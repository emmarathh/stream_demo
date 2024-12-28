import streamlit as st 

# Load data into DataFrame
df_combined_sorted_nonzero = pd.read_csv("df_combined_sorted_nonzero.csv")

st.title("Farm Meat Production Trends")

# Dropdown for selecting Meat Type
meat_type = st.selectbox("Select Meat Type", df_combined_sorted_nonzero["Meat Type"].unique())

# Filter the data for the selected meat type
df_filtered = df_combined_sorted_nonzero[df_combined_sorted_nonzero['Meat Type'] == meat_type]

# Plot the data
fig = px.line(df_filtered, x="Date", y="Value", color="Country", title=f"Meat Production Trends for {meat_type}")
st.plotly_chart(fig)