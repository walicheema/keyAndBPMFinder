from django.apps import AppConfig
from django.http import JsonResponse

class MyappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'myapp'
    
def index(request):
    return JsonResponse({'message': 'Welcome to the Key and BPM API!'})