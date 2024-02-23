import streamlit as st

import requests
import json
API_KEY = 'ceeb458124075676d8b43986e2514151'


st.title("Погода")

city = st.text_input("Введите название города", value="Калуга")

def fetch_weather_data(city):
    base_url = 'http://api.openweathermap.org/data/2.5/weather?'
    complete_url = f"{base_url}appid={API_KEY}&q={city}"
    response = requests.get(complete_url)
    return response.json()
 
def display_weather_data(weather_data):
    if weather_data['cod'] != '404':
        main_data = weather_data['main']
        # Convert from Kelvin to Celsius
        humidity = main_data['humidity']
        temperature = main_data['temp'] - 273.15 
        weather_description = weather_data['weather'][0]['description']

        return [round(temperature, 2), humidity, weather_description.capitalize()]

 
    else:
        return ["City not found. Please try again." * 3]
 
def main(city):

    weather_data = fetch_weather_data(city)
    return display_weather_data(weather_data)

st.metric(label = f"Погода в {city}", value =  main(city)[0])
