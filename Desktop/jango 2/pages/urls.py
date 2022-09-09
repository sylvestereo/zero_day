from django.urls import path
from pages import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add', views.add, name='ad.html'),
    path('about', views.about, name='about'),
    path('service', views.service, name='service'),
    path('contact', views.contact, name='contact'),
    path('blog' view.blog, name='blog'),
]