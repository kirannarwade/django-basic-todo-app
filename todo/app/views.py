from django.shortcuts import render, redirect
from app.models import Todo
from django.utils import timezone
from django.views import View
from datetime import datetime

# Create your views here.

class HomeView(View):
    def get(self, request):
        todo = Todo.objects.all()
        return render(request, "home.html", {'todo':todo})

    def post(self, request):
        if request.method == "POST":
            title = request.POST.get('title')
            desc = request.POST.get('desc')
            todo = Todo(title=title, desc=desc, date_time=timezone.now())
            todo.save()
            return redirect('/')
        return render(request, "home.html")

class UpdateView(View):
    def get(self, request, pk):
        todo = Todo.objects.get(pk=pk)
        return render(request, "update.html", {'todo':todo})

    def post(self, request, pk):
        if request.method == "POST":
            title = request.POST.get('title')
            desc = request.POST.get('desc')
            todo = Todo(pk=pk, title=title, desc=desc, date_time=timezone.now())
            todo.save()
            return redirect('/')

def deleteTodo(request, pk):
    todo = Todo.objects.get(pk=pk)
    todo.delete()
    return redirect('/')

def about(request):
    return render(request, "about.html")