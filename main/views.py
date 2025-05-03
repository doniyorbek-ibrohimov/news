from django.shortcuts import render
from django.views import View
from .models import *

class IndexView(View):
    def get(self,request):
        articles=Article.publisheds.order_by('-important','-views')
        context={
            'articles':articles
        }
        return render(request,'index.html',context)
