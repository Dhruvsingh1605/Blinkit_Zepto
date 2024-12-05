import requests
from datetime import datetime, timedelta
url = "https://api.openweathermap.org/data/2.5/forecast"


api_key = "307fbc63572f1ff852f9adede1d2b644"
latitude = 12.9716  
longitude = 77.5946  

params = {
    "lat": latitude,
    "lon": longitude,
    "appid": api_key,
    "units": "metric"  
}

response = requests.get(url, params=params)

if response.status_code == 200:
    data = response.json()

    today = datetime.now()
    day_after_tomorrow = (today + timedelta(days=1)).strftime('%Y-%m-%d')

    print(f"Weather forecast for tomorrow ({day_after_tomorrow}):\n")

    for forecast in data['list']:
        date = forecast['dt_txt'] 
        if day_after_tomorrow in date: 
            temperature = forecast['main']['temp'] 
            rainfall = forecast.get('rain', {}).get('3h', 0)  
            weather_description = forecast['weather'][0]['description']  

            print(f"Date & Time: {date}")
            print(f"Temperature: {temperature}°C")
            print(f"Rainfall (last 3 hours): {rainfall} mm")
            print(f"Weather: {weather_description}\n")

else:
    print(f"Error fetching data: {response.status_code}")
