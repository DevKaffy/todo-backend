from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, permission_required
from django.db import IntegrityError
from django.contrib import messages
from .models import Todo
from .forms import TodoEdit

# from django.views.generic import ListView, CreateView, UpdateView, DeleteView
# from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
# from django.urls import reverse_lazy
# from django.views.generic.edit import CreateView


# Create your views here.
def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Check if the username already exists
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Error, Username already exists')
            return redirect('register')
        try:
            new_user = User.objects.create_user(username=username, email=email, password=password)
            new_user.save()
            messages.success(request, 'User registered successfully')
            return redirect('login')
        except IntegrityError:
            messages.error(request, 'An error occurred. Please try again.')
            return redirect('register')
    return render(request, 'register.html')

@login_required
def todo(request):
    if request.method == 'POST':
        task = request.POST.get('task')
        new_todo = Todo(user=request.user, todo_name=task)
        new_todo.save()
    all_todos = Todo.objects.filter(user=request.user)
    context = {
        "todos" : all_todos,
    }
    return render(request, 'todo.html', context)



@permission_required("can_edit_task")
def edit(request, name):
    todo_item = get_object_or_404(Todo, user=request.user, todo_name=name)
    print(f"Requested edit for: {name}")
    if request.method == 'POST':
        form = TodoEdit(request.POST, instance=todo_item)
        if form.is_valid():
            form.save()
            return redirect('todo')  # Redirect to the list of todos
    else:
        form = TodoEdit(instance=todo_item)
    
    return render(request, 'edit.html', {'form': form})

def delete(request, name):
    get_todo = Todo.objects.filter(user=request.user, todo_name=name)
    get_todo.delete()
    return redirect('todo')

def update(request, name):
    get_todo = Todo.objects.get(user=request.user, todo_name=name)
    get_todo.status = True
    get_todo.save()
    return redirect('todo')



# Class based View

# class TodoListView(ListView):
#     model = Todo
#     template_name = 'todo.html'
    

# class TodoCreateView(LoginRequiredMixin, CreateView):
#     model = Todo
#     form_class = TodoEdit
#     template_name = 'todo.html'
#     success_url = reverse_lazy('todo')
#     login_url = 'login'

#     def form_valid(self, form):
#         form.instance.user = self.request.user
#         return super().form_valid(form)

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['todos'] = Todo.objects.filter(user=self.request.user)
#         return context



# class TodoUpdateView(LoginRequiredMixin, UpdateView):
#     model = Todo
#     form_class = TodoEdit
#     template_name = 'edit.html'
#     success_url = reverse_lazy('todo')
#     login_url = 'login'

#     def get_object(self, queryset=None):
#         name = self.kwargs.get('name')
#         return get_object_or_404(Todo, user=self.request.user, todo_name=name)