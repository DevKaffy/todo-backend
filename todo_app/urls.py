from django.urls import path
# from .views import TodoListView, TodoCreateView, TodoUpdateView
from . import views 
from django.contrib.auth import views as auth_views


# urlpatterns = [
#     path('todo/', TodoListView.as_view(), name='todo'),
#     path('todo/', TodoCreateView.as_view(), name='todo-create'),
#     path('todo/edit/<str:name>/', TodoUpdateView.as_view(), name='todo-edit'),
#     path('', views.register, name='register'),
#     path('login/', views.login, name='login'),
# ]



urlpatterns = [
    path('', views.register, name='register'),
    path('todo/', views.todo, name='todo'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('edit/<str:name>/', views.edit, name='edit'),
    path('delete/<str:name>/', views.delete, name='delete'),
    path('update/<str:name>/', views.update, name='update'),
]