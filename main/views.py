from django.shortcuts import render,redirect
from django.views import View
from .models import *
import requests

class IndexView(View):
    def get(self,request):
        articles=Article.publisheds.order_by('-important','-views')[:10]
        latest_articles=Article.publisheds.order_by('-created_at')[:10]
        most_views_articles=Article.publisheds.order_by("-views")[:10]
        moments=Moment.publisheds.order_by('-created_at')[:2]

        context={
            'articles':articles,
            'latest_articles':latest_articles,
            'most_views_articles':most_views_articles,
            'moments':moments,

        }
        return render(request,'index.html',context)
    def post(self,request):
        Newsletter.objects.create(
            email=request.POST.get('email'),
        )
        return redirect('index')
