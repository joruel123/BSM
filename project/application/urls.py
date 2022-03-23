from django.urls import path, include
from . import views

urlpatterns = [
path('', views.index, name='index'),
path('survey/',views.survey,name='survey'),
path('list/',views.list,name='list')
]