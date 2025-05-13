import requests
from .models import *
from django.db.models import Count
def get_weather(request):
    weather = requests.get('http://api.weatherapi.com/v1/current.json?q=fergana&key=3206b33f83b1486ea5c110109250702').json()
    return {
        'weather':weather
    }

def get_categories(request):
    categoties=Category.objects.annotate(article_count=Count('article')).order_by('-article_count')[:6]
    return {
        'categories':categoties
    }
