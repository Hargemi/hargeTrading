
from django.contrib import admin
from django.urls import path
from django.urls import include
from . import views  # Import views from the current app
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.tradingpago, name='tradingpago'),  # URL for the tradingpago view
]

