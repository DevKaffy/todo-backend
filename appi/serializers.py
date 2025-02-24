from todo_app.models import Todo
from rest_framework import serializers

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = '__all__'