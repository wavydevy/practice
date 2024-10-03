import json
import os
import requests
from dotenv import load_dotenv
from geopy import distance
import folium
from flask import Flask


def get_distance_from(current_list):
    return current_list['distance']


def fetch_coordinates(api, address):
    base_url = "https://geocode-maps.yandex.ru/1.x"
    response = requests.get(base_url, params={
        "geocode": address,
        "apikey": api,
        "format": "json",
    })
    response.raise_for_status()
    found_places = response.json()['response']['GeoObjectCollection']['featureMember']

    if not found_places:
        return None

    most_relevant = found_places[0]
    lon, lat = most_relevant['GeoObject']['Point']['pos'].split(" ")
    return lon, lat


def coffee_map():
    with open('index.html') as file:
        return file.read()


def main():
    with open('coffee.json', 'r', encoding='CP1251') as my_file:
        file_contents = my_file.read()
    contents = json.loads(file_contents)

    load_dotenv()
    apikey = os.getenv('API_KEY')

    user_location = str(input('Где вы находитесь?: '))
    user_coordinates = fetch_coordinates(apikey, user_location)
    user_longitude, user_latitude = user_coordinates
    user_coordinates = (user_latitude, user_longitude)

    database = []
    for content in contents:
        coffee_coordinates = (content['Latitude_WGS84'], content['Longitude_WGS84'])
        distance_from = distance.distance(user_coordinates, coffee_coordinates).km
        data = {
            'tittle': content['Name'],
            'distance': distance_from,
            'latitude': content['Latitude_WGS84'],
            'longitude': content['Longitude_WGS84']
        }
        database.append(data)

    database = sorted(database, key=get_distance_from)
    database = database[:5]

    m = folium.Map(location=(user_latitude, user_longitude), zoom_start=14)

    for data in database:
        folium.Marker(
            location=[data['latitude'], data['longitude']],
            tooltip="Coffee here!",
            popup="Mt. Hood Meadows",
            icon=folium.Icon(icon='cloud'),
        ).add_to(m)

    m.save("index.html")

    app = Flask(__name__)
    app.add_url_rule('/', 'Coffee nearby', coffee_map)
    app.run('0.0.0.0')


if __name__ == '__main__':
    main()
