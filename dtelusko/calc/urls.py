from django.urls import path

from . import views

urlpatterns = [
    path("",views.home, name="home"),
    #path("/add1",views.add1, name="add1"),
    #path("/add2",views.add2, name="add2"),
]