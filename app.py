import os
import streamlit as st
from datetime import datetime
from dotenv import load_dotenv
import time
import requests
from zoneinfo import ZoneInfo
load_dotenv()
API_KEY = os.getenv('API_KEY')
print("Enter the city name: ")
st.title("Weather App🌄")
city_name = st.text_input("City Name🌆",placeholder="City Name")
response = requests.get(f'http://api.openweathermap.org/geo/1.0/direct?q={city_name}&appid={API_KEY}')
try:
    lats = response.json()[0]['lat']
    longs = response.json()[0]['lon']
except KeyError:
    pass
try:
    weatherdata = requests.get(f'https://api.openweathermap.org/data/2.5/weather?lat={lats}&lon={longs}&appid={API_KEY}')
    description = weatherdata.json()['weather'][0]['description']
    temperature = round(weatherdata.json()['main']['temp'] - 273)
    feels_like = round(weatherdata.json()['main']['feels_like'] - 273)
    wind_speed = weatherdata.json()['wind']['speed']
    humidity = weatherdata.json()['main']['humidity']
    pressure = round((weatherdata.json()['main']['pressure'])*0.7500638)
    icon_id = weatherdata.json()['weather'][0]['icon']
    sunrise = weatherdata.json()['sys']['sunrise']
    sunrise_time = datetime.fromtimestamp(sunrise, tz=ZoneInfo("Asia/Kolkata"))
    sunset = weatherdata.json()['sys']['sunset']
    sunset_time = datetime.fromtimestamp(sunset, tz=ZoneInfo("Asia/Kolkata"))
    cod = weatherdata.json()['cod']
    cod =str(cod//100) + 'x'
    icon = f'https://openweathermap.org/img/wn/{icon_id}@{cod}.png'
    print(f'Weather: {description}\nTemperature: {temperature}\nFeels Like: {feels_like}\nWind Speed: {wind_speed}m/s\nPressure:{pressure}mmHg\nHumidity:{humidity}%\nIcon: {icon}')
    with st.status("Connecting to Weather..."):
        st.write("Searching for Data...")
        time.sleep(2)
        st.write("Found Data.")
        time.sleep(1)
        st.write("There you go...")
        time.sleep(1)
    unit = st.selectbox(
    "Select Celsius or Kelvin",
    ("Celsius", "Kelvin"),
    )
    st.image(icon)
    #st.write(f'Weather: {description}  \n : {temperature}°C  \n : {feels_like}°C  \n Wind Speed💨: {wind_speed}m/s  \n')
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Weather", f"{description}")
    with col2:
        st.metric("Wind Speed💨", f"{wind_speed}m/s")
    col1, col2 = st.columns(2)
    with col1:
        if (unit == 'Celsius'):
            st.metric("Temperature🌡️", f"{temperature}°C")
        else:
            st.metric("Temperature🌡️", f"{temperature+273}K")
    with col2:
        if (unit == 'Celsius'):
            st.metric("Feels Like☀️", f"{feels_like}°C")
        else:
            st.metric("Feels Like☀️", f"{feels_like+273}K")
    col1,col2 = st.columns(2)
    with col1:
        st.metric("Sunrise 🌅:", sunrise_time.strftime("%I:%M %p"))
    with col2:
        st.metric("Sunset 🌇:", sunset_time.strftime("%I:%M %p"))
    col1,col2 = st.columns(2)
    with col1:
        st.metric("Humidity", f'{humidity}%')
    with col2:
        st.metric("Pressure",f'{pressure}mmHg')
    st.balloons()
    st.html("<footer>The Timezone is With Respect To Indian Standard Time</footer>")
except NameError:
    pass