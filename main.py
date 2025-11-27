import requests
import matplotlib.pyplot as plt

API_KEY = "0feca5ac662f4b2390a105910252711"
CITY = "Bengaluru"
FORECAST_DAYS = 1
URL = f"http://api.weatherapi.com/v1/forecast.json?key={API_KEY}&q={CITY}&days={FORECAST_DAYS}&aqi=no&alerts=no"

try:
    response = requests.get(URL)
    response.raise_for_status()
    data = response.json()

    hourly_forecasts = data['forecast']['forecastday'][0]['hour']
    
    hours_to_plot = 12
    times = [f['time'].split(' ')[1] for f in hourly_forecasts[:hours_to_plot]]
    temperatures = [f['temp_c'] for f in hourly_forecasts[:hours_to_plot]]

    plt.figure(figsize=(12, 6))
    plt.plot(times, temperatures, marker='o', linestyle='-', color='b')
    plt.xlabel('Time of Day')
    plt.ylabel('Temperature (°C)')
    plt.title(f'Next {hours_to_plot} Hours Temperature Forecast for {CITY}')
    plt.xticks(rotation=45, ha='right')
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.show()
    plt.savefig(f'{CITY}_Temperature_Forecast.png')

except requests.exceptions.RequestException:
    pass
except KeyError:
    pass
