import requests
import json

def init():
    url = "https://restcountries-v1.p.rapidapi.com/all"
    headers = {
    'x-rapidapi-host': "restcountries-v1.p.rapidapi.com",
    'x-rapidapi-key': "0cffd7d40amshdcd1956b2a2fb7ep10bb62jsnc9dd7091d943"
    }
    print("Inside get all country")
    response = requests.request("GET", url, headers=headers)
    return response.text
def getCountry(name):
    url = "https://restcountries-v1.p.rapidapi.com/name/"+name
    headers = {
    'x-rapidapi-host': "restcountries-v1.p.rapidapi.com",
    'x-rapidapi-key': "0cffd7d40amshdcd1956b2a2fb7ep10bb62jsnc9dd7091d943"
    }
    print("Inside get country by name")
    response = requests.request("GET", url, headers=headers)
    return response.text
def getCountryByCapital(city):
    url = "https://restcountries-v1.p.rapidapi.com/capital/"+city
    headers = {
    'x-rapidapi-host': "restcountries-v1.p.rapidapi.com",
    'x-rapidapi-key': "0cffd7d40amshdcd1956b2a2fb7ep10bb62jsnc9dd7091d943"
    }
    response = requests.request("GET", url, headers=headers)
    return response.text


