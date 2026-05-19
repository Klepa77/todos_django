from .models import Todo
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
from .utils import get_russian_date




def hello_world(request):
    return HttpResponse('Hello, World!')


def home_page(request):
    return HttpResponse('Home Page')

def index(request):
    current_date = get_russian_date()
    todos = Todo.objects.all().order_by('is_completed')
    return render(request, 'index.html',{'current_date':current_date,
                                         'todos':todos})

def add_todo(request):
    text = request.POST.get('text')
    deadline = request.POST.get('deadline')
    Todo.objects.create(text=text,deadline=deadline)
    return redirect('app:index')


def complete_todo(request,pk):
    pass

def delete_todo(request, pk):
    if request.method == 'POST': # Рекомендуется удалять через POST
        todo = get_object_or_404(Todo, pk=pk)
        todo.delete()
        return JsonResponse({
            'status': 'success',
            'id': pk,
            'message': 'Задача успешно удалена'
        })
    return JsonResponse({'status': 'error'}, status=400)