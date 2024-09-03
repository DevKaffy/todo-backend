from django import forms
from .models import Todo

class TodoEdit(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['todo_name', 'scheduled_date', 'due_date', 'status']
    widgets = {
            'todo_name': forms.TextInput(attrs={'class': 'form', 'placeholder': 'Enter task title'}),
            'status': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'due_date': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
            'assigned_to': forms.Select(attrs={'class': 'form-control'}),
        }
    