import requests
import datetime
import json

print("Hello World")

city = input("Can you put your city? ")
api = "your-token"
url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api}&units=metric"

req = requests.get(url)
data = req.json()

conver=json.dumps(data, indent=4)
print(conver)

if req.status_code == 200:
    date= datetime.datetime.now()
    print(date)
    temp = data["main"]["temp"]
    wind = data["wind"]["speed"]
    description = data['weather'][0]['description']
    print(f"Weather in {city}: {temp}°C the wind speed is :  {wind}, {description}")

    print(temp)
else:
    print("City not found or there was an error")
