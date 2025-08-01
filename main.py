from opencage.geocoder import OpenCageGeocode
from pygments.lexers.sql import language_re


def get_coordinates(city, key):
    try:
        geocoder = OpenCageGeocode(key)
        results = geocoder.geocode(city, language='ru')
        if results:
            lat = round(results[0]['geometry']['lat'], 2)
            lon = round(results[0]['geometry']['lng'], 2)
            return f'Широта: {lat}, Долгота: {lon}'
        else:
            return 'Город не найден'
    except Exception as e:
        return f'Возникла ошибка : {e}'



key = '3ebb6a43f72d4de090e915d62e03e30e'
city = 'Мурманск'
coordinates = get_coordinates(city, key)
print(f'Координаты города {city}: {coordinates}')

