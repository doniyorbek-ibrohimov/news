from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from main.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',IndexView.as_view(),name='index'),
    path('newsletter-create/',NewsletterCreateView.as_view()),
    path('articles/<slug:slug>/',ArticleDetailView.as_view(),name="detail_page"),
    path('contact/',ContactView.as_view(),name="contact"),
    path('category/<int:pk>/', CategoryArticleListView.as_view(), name='category_articles'),

]

urlpatterns +=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)