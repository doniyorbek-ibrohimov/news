from django.http import HttpResponse
from django.urls import reverse
from django.shortcuts import render,redirect,get_object_or_404
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

class ArticleDetailView(View):
    def get(self,request,slug):
        article=get_object_or_404(Article,slug=slug)
        comments=Comment.objects.all().order_by('-created_at')
        context={
            'article':article,
            'comments':comments
        }
        return render(request,'detail-page.html',context)
    def post(self,request,slug):
        article=get_object_or_404(Article,slug=slug)
        Comment.objects.create(
            article=article,
            name=request.POST.get('name'),
            email=request.POST.get('email'),
            text=request.POST.get('text')
        )
        article.comments +=1
        article.save()
        return redirect('detail_page',slug=slug)

class ContactView(View):
    def get(self,request):
        return render(request,'contact.html')

    def post(self,request):
       Contact.objects.create(
           name=request.POST.get('name'),
           email=request.POST.get('email'),
           phone=request.POST.get('phone'),
           subject=request.POST.get('subject'),
           message=request.POST.get('message')
       )
       home_url = reverse('index')
       return HttpResponse(f"Contact was added successfully <br> <a href='{home_url}'>Back to Home Page</a>")

class CategoryArticleListView(View):
    def get(self, request, pk):
        category = get_object_or_404(Category, pk=pk)
        articles = Article.publisheds.filter(category=category).order_by('-created_at')
        return render(request, 'category_articles.html', {
            'category': category,
            'articles': articles
        })

class NewsletterCreateView(View):
    def post(self,request):
        Newsletter.objects.create(
            email=request.POST.get('email')
        )
        return redirect('index')

