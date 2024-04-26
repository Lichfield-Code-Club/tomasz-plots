# tomasz-plots
Graph plots from UK Met Office weather data

## Basic Plot

* Fixed array of data
* Random array of data
* Met Ofice data
  * Pulled from internet and saved to file
  * Data extracted from file

## User Interface

* Flask framework
* Met Office stations
* Met Office data
* Ask User for
  * Which year
  * Which data: rainfall, min temp, etc
  * Plot type: histogram, line etc
  * Display selected data
  * Maybe 2 lines: min temp and max temp?

## Required python modules
pip install beautifulsoup4 fastapi jinja2 uvicorn plotly pandas python-multipart

## To run the webserver

In a terminal window: uvicorn weather:app --reload
IF this doesn't work: python3 -m uvicorn weather:app --reload

## To explore the app
open http://127.0.0.1:8000/weather in a browser.
Currently the available dates are 
# Dummy weather data
weather_data = {
    "2021-01-01": {"temperature": 5, "description": "Sunny"},
    "2021-01-02": {"temperature": 3, "description": "Cloudy"},
    "2021-01-03": {"temperature": -1, "description": "Snowy"},
    "2024-04-19": {"temperature": -1, "description": "Snowy"},
    "2024-04-20": {"temperature": -1, "description": "Snowy"},
    "2024-04-21": {"temperature": -1, "description": "Snowy"},
    # Add more data as needed
}

## To view the available 'routes'

in a browser, open http://127.0.0.1:8000/docs#/
To refresh all of the station data chose the 'GET' /refresh/data option, click on 'Try it Out' and then click on Execute.
If all is well you should have all the weather station data in files in the data folder

To See the data for a particular station: Click on 'GET' /station/data, Try it Out and in the station name put in one of the station names that were downloaded e.g. cardiff

To see a sample plot, Click 'GET' /plot, Try it Out, Execute
