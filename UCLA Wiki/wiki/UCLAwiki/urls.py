from django.urls import path
from . import views


urlpatterns = [
    path("index", views.home),
    path("<str:name>", views.index)
    
    #path("", views.index)
]