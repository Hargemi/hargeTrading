
from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
   
     path('', views.tradingfree, name='tradingfree'),  # URL for the tradingfree view
    
]

