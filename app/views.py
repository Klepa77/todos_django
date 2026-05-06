from .models import Todo
from django.shortcuts import render
from django.http import HttpResponse
from .utils import get_russian_date


def hello_world(request):
    return HttpResponse('Hello, World!')


def home_page(request):
    return HttpResponse('Home Page')

def index(request):
    current_date = get_russian_date()
    todos = Todo.objects.all()
    return render(request, 'index.html',{'current_date':current_date,
                                         'todos':todos})
