from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TaskListView, LoginView
from todo_app.models import Todo
from .serializers import TaskSerializer


router = DefaultRouter()
router.register('tasklist', TaskListView, basename='tasklist')

urlpatterns = [
    # path('', include(router.urls)),
    path('', TaskListView.as_view(queryset=Todo.objects.all(), serializer_class=TaskSerializer)),
    path('login/', LoginView.as_view(), name='login'),
    
]