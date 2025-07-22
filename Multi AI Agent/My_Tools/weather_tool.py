from agents import function_tool
from dotenv import load_dotenv
import os
import requests



load_dotenv(override= True)
API_KEY = os.getenv("WEATHER_API_KEY")



@function_tool
def get_weather(city:str) -> str:
    """
    fetch weather api 
    and return in string format"""


    BASEURL = "http://api.weatherapi.com/v1/current.json"
    

    url = f"{BASEURL}?key={API_KEY}&q={city}"
    req_res = requests.get(url)
    DATA = req_res.json()



    reply =f"\The current weather in {DATA['location']['name']} is {DATA['current']['temp_c']}°C with {DATA['current']['condition']['text']}."
    return  reply