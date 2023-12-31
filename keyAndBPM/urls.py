"""
URL configuration for keyAndBPM project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from myapp.views import get_tempo, get_key
from myapp import views
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['POST'])
def default(request):
     return Response("Reached endpoint")
 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('get_tempo/', get_tempo, name= 'get_tempo'),
    path('', default, name= 'default'),
    path('get_key/', get_key, name='get_key'),
]


    
