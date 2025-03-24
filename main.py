import requests #Requests library : popular for requesting https : fetching web pages, apis etc
import json #allows working with json data | here the weather api was in json format |
import pyttsx3 #text to speech conversion

city = input("Enter City: \n")

url = f'http://api.weatherapi.com/v1/current.json?key=b11927568b3849d39ce73310252003&q={city}'

r = requests.get(url)

engine=pyttsx3.init() #initializing the tts module
engine.setProperty('rate', 135)

wdict = json.loads(r.text) #convert json-formatted string to python object(dictionary, list)

engine.say(f'Here is the weather details of {city}: ')
engine.runAndWait()

print("Temperature in Celsius: ")
print(wdict["current"]["temp_c"])
print("Weather condition: ")
print(wdict["current"]["condition"]["text"])
print(wdict["current"]["wind_kph"])

weather_report = (
    f'The temperature is {wdict["current"]["temp_c"]} degrees celsius and'
    f'The weather condition is {wdict["current"]["condition"]["text"]}'
    f'The wind speed is {wdict["current"]["wind_kph"]} kilometers per hour.'
)

engine.say(weather_report)
engine.runAndWait()
