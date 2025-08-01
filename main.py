from opencage.geocoder import OpenCageGeocode


def get_coordinates(city, key):
    geocoder = OpenCageGeocode(key)
    query = city
    results = geocoder.geocode(query)
    if results:
        return results[0]['geometry']['lat'], results[0]['geometry']['lng']
    else:
        return 'Город не найден'


key = '3ebb6a43f72d4de090e915d62e03e30e'
city = 'Moscow'
coordinates = get_coordinates(city, key)
print(f'Координаты города {city}: {coordinates}')

