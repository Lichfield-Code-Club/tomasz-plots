from stations import stations, station_file, station_data
import plotly.express as px

def locations(all_stations):
    return [d['station'] for d in all_stations]

def location_data(all_data,station,fname):
    href = [d['href'] for d in all_data if d['station'] == station][0]
    html = station_file(href=href,fname=fname)
    return station_data(fname=fname)

if __name__ == '__main__':
    fname = 'data/station_stations.json'
    all_stations = stations(fname=fname)
    all_locations = locations(all_stations=all_stations)

    # Try getting first set of data
    chosen_station = all_locations[0]
    station_fname = f'data/{chosen_station}_data.txt'
    print(f'Extracting Data for {chosen_station} to {station_fname}')
    info = location_data(all_data=all_stations,station=chosen_station,fname=station_fname)

    # Display a line plot for rainfall in 1957
    months = [x['month'] for x in info if x['year'] == 1957]
    rainfall = [x['rain'] for x in info if x['year'] == 1957]

    # print(rainfall)
    # print(months)
    fig = px.line(x=months, y=rainfall)
    fig.show()