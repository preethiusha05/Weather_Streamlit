import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Page title
st.title("Weather Dashboard")

# Weather icon
st.image("C:\weather_dashboard\Wallpaper_ Cloudy mood Wallpaper_.jpg", width=120)

# Load dataset
df = pd.read_csv("weatherHistory.csv")

# Remove column spaces if any
df.columns = df.columns.str.strip()

# Show dataset
st.subheader("Weather Dataset")
st.dataframe(df.head())

# City selection
st.subheader("Select City")
city = st.selectbox("Choose a city", df["City"].unique())

# Filter data by city
city_data = df[df["City"] == city]

st.write("Data for", city)
st.dataframe(city_data.head())

# Weather Metrics
st.subheader("Weather Metrics")

st.metric("Average Temperature (°C)", round(city_data["Temperature (C)"].mean(),2))
st.metric("Average Humidity", round(city_data["Humidity"].mean(),2))
st.metric("Average Wind Speed (km/h)", round(city_data["Wind Speed (km/h)"].mean(),2))

# Temperature Chart
st.subheader("Temperature Chart")

st.line_chart(city_data["Temperature (C)"])

# Humidity Chart
st.subheader("Humidity Chart")

st.bar_chart(city_data["Humidity"])

# Pie Chart
st.subheader("Temperature Distribution")

fig, ax = plt.subplots()
ax.pie(city_data["Temperature (C)"].head(10),
       labels=city_data["Summary"].head(10),
       autopct="%1.1f%%")

st.pyplot(fig)

# User input
name = st.text_input("Enter your name")

if name:
    st.success(f"Hello {name}, welcome to the Weather Dashboard!")