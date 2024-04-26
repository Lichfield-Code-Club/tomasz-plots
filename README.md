# tomasz-plots
Graph plots from UK Met Office weather data

## Basic Plot

* Met Ofice data
  * Pulled from internet and saved to file
  * Data extracted from file

## User Interface

* FastApi framework
* Met Office stations
* Met Office data
* Ask User for
  * Which year
  * Which data: rainfall, min temp, etc
  * Plot type: histogram, line etc
  * Display selected data
  * Maybe 2 lines: min temp and max temp?

## Required python modules

* pip install -r requirements.txt

## Run the webserver

In a terminal window, one of:
* uvicorn weather:app --reload
* python3 -m uvicorn weather:app --reload

## Explore the app

The link below requires a start date and an end date.
Select these dates from Sample Weather Data

[weather](http://127.0.0.1:8000/)

# Sample Weather Data
```json
"weather-data":  {
    "2021-01-01": {"temperature": 5, "description": "Sunny"},
    "2021-01-02": {"temperature": 3, "description": "Cloudy"},
    "2021-01-03": {"temperature": -1, "description": "Snowy"},
    "2024-04-19": {"temperature": -1, "description": "Snowy"},
    "2024-04-20": {"temperature": -1, "description": "Snowy"},
    "2024-04-21": {"temperature": -1, "description": "Snowy"}
}
```

## Weather App Features

 ![Weather App API calls](/assets/fastapi-docs.png)
 
 ![Weather Data](/assets/get-weather-data.png)
 
 ![Station Data](/assets/get-station-data.png)
 
 ![Select Data](/assets/get-root.png)
 
 ![Plot Data](/assets/get-plot.png)
 
Open the documentation ![web page](http://127.0.0.1:8000/docs#/)

* For each of the features listed below
 * Click on GET
 * Click on Try It Out
 * Click on Execute

Features
 * ![Weather Data](/assets/get-weather-data.png)
 * ![Station Data](/assets/get-station-data.png)
 * ![Select Data](/assets/get-root.png)
 * ![Plot Data](/assets/get-plot.png)

If all is well you should have all the weather station data in files in the data folder
