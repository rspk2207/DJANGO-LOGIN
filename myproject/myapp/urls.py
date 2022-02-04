from unicodedata import name
from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name = "index"),
    path('reg',views.reg,name = "reg"),
    path('login',views.login,name = "login"),
    path('home',views.home,name = "home"),
    path('home/about',views.about,name="about"),
    path('logout',views.logout,name="logout"),
    path('home/dashboard',views.dashboard,name="dashboard")

]