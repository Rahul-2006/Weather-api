# 🌤️ Weather App - Streamlit + OpenWeatherMap
<br>
A simple and interactive weather web app built using <strong>Streamlit</strong> and <strong>OpenWeatherMap API</strong>. You have to enter the name of a city and get real-time weather updates, including temperature, humidity, wind speed, sunrise/sunset times, and more!! <br>


## Features

- 🌆 Enter any city to fetch real-time weather data <br>
- 🌡️ Temperature and "Feels Like" in Celsius or Kelvin <br>
- 💨 Wind speed, humidity, and pressure <br>
- 🌅 Sunrise and 🌇 sunset times (in IST) <br>
- 📷 Weather condition icons <br>
- 🎈 Streamlit balloons for fun! <br>

## Setup <br>

### 1. Clone the repo <br>
```bash 
git clone https://github.com/your-username/weather-app.git
cd weather-app
```
<br>

### 2. Install Virtual Environment <br>

```bash 
python -m venv venv
venv\Scripts\activate
```
<br>

### 3. Install all the dependencies <br>

```bash
python -r requirements.txt
```
<br>

### 4. Set Up Your OpenWeatherMap API Key <br>
- Go to https://openweathermap.org/api <br>
- Sign up and create an API key <br>
- Create a .env file in the project root with the following content: <br>
- API_KEY=created_api_key <br>

### 5. Run the streamlit app <br>
```bash
streamlit run app.py
```
