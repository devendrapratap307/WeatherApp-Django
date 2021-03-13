from django.http import HttpResponse
from django.shortcuts import render, Http404
import requests
import urllib.request
import json

baseUrl = "https://api.openweathermap.org/data/2.5/weather?appid=520e022eeb2cd78250b831a7d8ecc898&q="


# Create your views here.
##  these two functions( split_string and join_string ) is only for join more than 1 city names with +
def split_string(city):
    # Split the string based on space delimiter
    list_city = city.split(' ')
    return list_city


def join_string(list_city):
    # Join the string based on '+' delimiter
    string = str('+'.join(list_city))
    return string


## Create your views here.
def home(request):
    if request.method == 'POST' or None:
        city = request.POST['city']

        list_city = split_string(city)
        strCity = join_string(list_city)

        apiUrl = baseUrl + strCity
        source = urllib.request.urlopen(apiUrl).read()
        content = json.loads(source)


        # taking out necessary data from json
        weather = content['weather'][0]['description']
        temp = content['main']['temp']
        country = content['sys']['country']
        name = content['name']
        icon = content['weather'][0]['icon']
        wind_spd = content['wind']['speed']
        pressure = content['main']['pressure']
        humidity = content['main']['humidity']
        cloud = content['clouds']['all']

        # send response to template
        data = {
                'weather': weather,
                'temp': "{:.2f}".format(temp - 273.15),
                'country': country,
                'name': name,
                'icon': icon,
                'windSpeed': wind_spd,
                'pressure': pressure,
                'humidity': humidity,
                'cloud': cloud,
        }


    else:
        # if data not found
        data = {}
    return render(request, 'weather1/home.html', data)
