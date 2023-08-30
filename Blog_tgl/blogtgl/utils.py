import requests

def get_countries_from_api():
    response = requests.get('https://restcountries.com/v3.1/all')
    data = response.json()
    countries = [country['name']['common'] for country in data]
    return countries
