from django.urls import path
from mainwebsite import views

urlpatterns = [
    path('', views.index, name='index'),
]