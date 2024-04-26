from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from datetime import datetime
from stations import refresh_station_data, station_data
from plot import sample_plot

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

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

@app.get("/refresh/data",response_class=HTMLResponse)
async def refresh_data(request: Request):
    # Real weather data
    stations = refresh_station_data()
    return templates.TemplateResponse("stations.html", {
        "request": request,
        "station_list": stations
        }
    )

@app.get("/station/data",response_class=HTMLResponse)
async def text_data(station_name: str, request: Request):
    datadir = 'data'
    datafile = f'{datadir}/{station_name}data.txt'
    data = station_data(datafile)
    return templates.TemplateResponse("data.html", {
        "data": data,
        "request": request
        }
    )

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})
    
@app.post("/weather", response_class=HTMLResponse)
async def get_weather(request: Request, start_date: str = Form(...), end_date: str = Form(...)):
    # Convert string dates to datetime objects
    start_date = datetime.strptime(start_date, "%Y-%m-%d")
    end_date = datetime.strptime(end_date, "%Y-%m-%d")
    
    # Filter weather data within the date range
    filtered_weather_data = {
        date: data for date, data in weather_data.items()
        if start_date <= datetime.strptime(date, "%Y-%m-%d") <= end_date
    }
    
    return templates.TemplateResponse(
        "weather.html",
        {
            "request": request,
            "weather_data": filtered_weather_data,
            "start_date": start_date,
            "end_date": end_date
        }
    )

@app.get("/plot", response_class=HTMLResponse)
async def get_weather(request: Request):
    x=["a", "b", "c"]
    y=[1, 3, 2]
    sample_plot(x,y)

