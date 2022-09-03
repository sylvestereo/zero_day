from django.urls import path
from api import views


urlpatterns = [
    path('createapi', views.createapi, name='createapi'),
    path('allapi', views.allapi, name='allapi'),
    path('deleteapi/<int:id>', views.deleteapi, name='deleteapi'),
    path('apidetail/<int:id>', views.apidetail, name='apidetail'),
    path('apiedit/<int:id>', views.apiedit, name='apiedit')
]