from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='personalarea'),
    path('categories', views.categories, name='categories'),
    path('main', views.main, name='main'),
    path('about', views.about, name='about'),
    path('blog', views.blog, name='blog'),
    path('contact', views.contact, name='contact'),
    path('id=<id>&username=<username>', views.single_list, name='single-list'),
    path('search', views.search, name='search'),
]