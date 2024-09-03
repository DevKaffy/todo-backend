from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Todo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    todo_name = models.CharField(max_length=1000)
    status = models.BooleanField(default=False)
    # created_by = models.ForeignKey(User, related_name = 'created_tasks', on_delete=models.SET_NULL, null=True, blank=True)
    # assigned_to = models.ForeignKey(User, related_name = 'assigned_to', on_delete=models.SET_NULL, null=True, blank=True)
    scheduled_date = models.DateField()
    due_date = models.DateField()

    class Meta:
        permissions = [("can_edit_task", "Can_edit_task"), ("can_delete_task", "Can_delete_task")]

    def __str__(self):
        return self.todo_name