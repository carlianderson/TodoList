from django.shortcuts import render, get_object_or_404
from .models import TodoList, Category, User
from django.urls import reverse_lazy
from .forms import CategoryForm, TaskForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect


# Create your views here.
def index(request):
    return render(request, 'todoapp/index.html')

def todo(request):
    todo_list=TodoList.objects.all()
    return render(request, 'todoapp/todo.html', {'todo_list' : todo_list})
   
def tododetail(request, id):
    todo=get_object_or_404(TodoList, pk=id)
    return render(request, 'todoapp/tododetail.html', {'todo' : todo})

def newTask(request):
     form=TaskForm
     if request.method=='POST':
          form=TaskForm(request.POST)
          if form.is_valid():
               post=form.save(commit=True)
               post.save()
               form=TaskForm()
     else:
          form=TaskForm()
     return render(request, 'todoapp/newtask.html', {'form': form})

def deleteTask(request, t):
    task = TodoList.objects.get(id= t)
    task.delete()
    return HttpResponseRedirect('/todoapp/todo/') 

@login_required  
def newCategory(request):
     form=CategoryForm
     if request.method=='POST':
          form=CategoryForm(request.POST)
          if form.is_valid():
               post=form.save(commit=True)
               post.save()
               form=CategoryForm()
     else:
          form=CategoryForm()
     return render(request, 'todoapp/newcategory.html', {'form': form})

def loginmessage(request):
    return render(request, 'todoapp/loginmessage.html')

def logoutmessage(request):
    return render(request, 'todoapp/logoutmessage.html')