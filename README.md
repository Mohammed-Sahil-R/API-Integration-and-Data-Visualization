# API-Integration-and-Data-Visualization
COMPANY: CODTECH IT SOLUTIONS

NAME: MOHAMMED SAHIL R

INTERN ID: CT04DR1393

DOMAIN: PYTHON PROGRAMMING

DURATION: 4 WEEKS

MENTOR: NEELA SANTOSH

## Objective:
Fetch weather forecast data for Bengaluru and visualize key metrics like temperature, humidity, and wind speed.

## API Selection and Integration:
The WeatherAPI was chosen as the public data source. The Python script uses the requests library to send HTTP GET requests. A dedicated function handles the API call, passing the API key and target city (Bengaluru) to retrieve forecast data in JSON format. Error handling ensures the script is robust and handles network or HTTP errors gracefully.

## Data Extraction and Parsing:
The JSON response is converted into a Python dictionary. The script extracts hourly forecast data for the next 24 hours, including time stamps and temperature in Celsius.

## Data Preparation for Plotting:
Time strings are formatted to show only the hour (e.g., '10:00') for readability. The first 12–24 hourly data points are selected to focus on the short-term forecast.

## Visualization Dashboard Creation:
Matplotlib is used to generate a line plot for the hourly temperature. The figure size is 12 × 6 inches, with labeled axes (Time of Day and Temperature (°C)) and a descriptive title for Bengaluru. Grid lines, markers, and color enhancements improve readability. The x-axis labels are rotated 45° to prevent overlap. The final visualization is saved as Bengaluru_Temperature_Forecast.png and displayed.


# OUTPUT 
<img width="1200" height="600" alt="Image" src="https://github.com/user-attachments/assets/313eac9f-c184-4700-855d-d9888e8e571e" />
