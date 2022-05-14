from django.urls import path
from . import views


urlpatterns = [
    path("homepage", views.home, name="home"),
    path("random", views.randomentry, name="random"),
    path("entry/<str:name>", views.index, name="entry"),
    path("newentry", views.newentry, name="newentry"),
    path("saveentry", views.saveentry, name="saveentry"),
    path("editentry/<str:entryname>", views.editentry, name="editentry"),
    path("saveedit", views.saveedit, name="saveedit")
]