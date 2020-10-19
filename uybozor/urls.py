from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('categories', views.categories, name='categories'),
    path('contact', views.contact, name='contact'),
    path('search', views.search, name='search'),
    path('blog', views.blog, name='blog'),
]