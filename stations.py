from bs4 import BeautifulSoup
from urllib.request import urlopen
import json
import re


def stations(fname):
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
            results["opened"] = aux[2].string
            results["href"] = aux[3].find('a')['href']
            data.append(results)

    with open(fname, 'w') as f:
        json.dump(data, f,sort_keys=True,indent=4, ensure_ascii=True)
        
    return data

def station_file(href,fname):
    page = urlopen(href)
    html = page.read().decode("utf-8")

    with open(fname,'w') as fw:
        fw.write(html)
    return html

def station_data(fname):
    with open(fname,'r') as fr:
        lines  = fr.readlines()
    lines = [line for line in lines if re.match(r'^\s{3}([1-3][0-9]{3})',line)]
    data = []
    for line in lines:
        row = {}
        row['year']  = int(line[:9].strip())
        row['month'] = int(line[9:12].strip())
        row['tmax']  = line[14:18].strip()
        row['tmin']  = line[19:29].strip()
        row['af']    = line[30:35].strip()
        row['rain']  = float(line[36:43].strip())
        row['sun']   =  line[45:].strip()
        data.append(row)
    return data