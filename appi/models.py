from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Todo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='appi_todos')
    todo_name = models.CharField(max_length=1000)
    status = models.BooleanField(default=False)
    scheduled_date = models.DateField()
    due_date = models.DateField()


    def __str__(self):
        return self.todo_name