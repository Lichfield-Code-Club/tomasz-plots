from bs4 import BeautifulSoup
from urllib.request import urlopen
import json
import re
import os

def stations(fname) -> list [dict]:
    url = "https://www.metoffice.gov.uk/research/climate/maps-and-data/historic-station-data"

    page = urlopen(url)
    html = page.read().decode("utf-8")
    soup = BeautifulSoup(html, "html.parser")

    data = []
    for row in soup.findAll('tr'):
        aux = row.findAll('td')
        if aux:
            results = {}
            results["station"] = aux[0].string
            results["location"] = aux[1].string
            results["openend"] = aux[2].string
            results["href"] = aux[3].find('a')['href']

            textfile = os.path.basename(results['href'])
            textfile = f'data/{textfile}'
            jsonfile = textfile.replace('.txt','.json')
    

            results['text'] = textfile
            results['json'] = jsonfile
            data.append(results)

    with open(fname, 'w') as f:
        json.dump(data, f,sort_keys=True,indent=4, ensure_ascii=True)
        
    return data

def station_file(href: str,fname: str):
    page = urlopen(href)
    html = page.read().decode("utf-8")
    with open(fname,'w') as fw:
        fw.write(html)
    return html

def raw_data(infile: str) -> list[str]:
    with open(infile,'r') as fr:
        lines  = fr.readlines()
    return lines

def raw_html(lines: list[str]) -> list[str]:
    lines = [x.strip() for x in lines]
    return lines

def filtered_data(infile: str) -> list [str]:
    lines = raw_data(infile=infile)
    return [line for line in lines if re.match(r'^\s{3}([1-3][0-9]{3})',line)]


def save_json(fname: str, data: str) -> None:
    with open(fname, 'w') as f:
        json.dump(data, f,sort_keys=True,indent=4, ensure_ascii=True)

def station_data(infile: str):
    lines = filtered_data(infile=infile)
    data = []
    for line in lines:
        row = {}
        weather_data = line.split(' ')
        row['year']  = weather_data[0]
        row['month'] = weather_data[1]
        row['tmax']  = weather_data[2]
        row['tmin']  = weather_data[3]
        row['af']    = weather_data[4]
        row['rain']  = weather_data[5]
        row['sun']   = weather_data[6]
        data.append(row)
    return data

def refresh_station_data() -> dict:
    datadir = 'data'
    fname = f'{datadir}/station_stations.json'
    weather_stations = stations(fname=fname)

    for station in weather_stations:
        text_fname = station['text']
        json_fname = station['json']
        station_file(fname=text_fname, href=station['href'])
        data = station_data(infile=text_fname)
        save_json(fname=json_fname,data=data)
    return weather_stations