import requests

def get_weather(request):
    weather = requests.get('http://api.weatherapi.com/v1/current.json?q=fergana&key=3206b33f83b1486ea5c110109250702').json()
    return {
        'weather':weather
    }


