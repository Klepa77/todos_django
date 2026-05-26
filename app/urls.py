from django.urls import path
from . import views
urlpatterns = [
    path('hello_world/',views.hello_world),
    path('home',views.home_page),
    path('',views.index,name='index'),
    path('add_todo',views.add_todo,name='add_todo'),
    path('delete_todo/<int:pk>',views.delete_todo,name='delete_todo'),
    path('finish_todo/<int:pk>',views.finish_todo,name = 'finish_todo'),
    path('get_todo/<int:pk>',views.get_todo,name='get_todo'),
    path('update_todo/<int:pk>',views.update_todo,name='update_todo'),


]