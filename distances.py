import json
import requests


def get_key(path, index):
    """Gets api key from a json file.

    Args:
        path (string): the file path to the json file containing the api keys
        index (int): the index of the key to be returned

    Returns:
        string: the key at the index specified
    """
    with open(path) as f:
        return list(json.load(f).values())[index]


KEY_PATH = "credentials.json"
LAT_1 = 40.6655101
LON_1 = -73.89188969999998
LAT_2 = 40.6905615
LON_2 = -73.9976592

key = get_key(KEY_PATH, 0)

try:
    url = f"https://maps.googleapis.com/maps/api/distancematrix/json?units=imperial&origins={LAT_1},{LON_1}&destinations={LAT_2}%2C{LON_2}&key={key}"
    r = requests.get(url)
    data = r.json()
    print(
        f"Road distance between {LAT_1}, {LON_1} and {LAT_2}, {LON_2}: {data['rows'][0]['elements'][0]['distance']['text'].replace(' mi', '')} miles")
except:
    print("Request failed")
