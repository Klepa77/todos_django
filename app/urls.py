from django.urls import path
from . import views
urlpatterns = [
    path('hello_world/',views.hello_world),
    path('home',views.home_page),
    path('',views.index),

]