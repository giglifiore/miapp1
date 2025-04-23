from django.http import HttpResponse
from django.urls import path
from home.views import hola
def home(request):
    return HttpResponse("Hola mundo desde Django en Render!")

urlpatterns = [
    path('', home),
    path('', hola),
]
