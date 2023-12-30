from django import forms
from .models import TaskModel

class TaskForm(forms.ModelForm):
    class Meta:
        model= TaskModel
        fields = '__all__'
        label = {
            'task_title': 'Task Title',
            'task_description': 'Task Description',
            'is_completed' : 'Task Status',
            'assign_date' : 'Task Assignment Date',
        }
        widgets = {
            'assign_date': forms.DateTimeInput({'type': 'date'}),
        }

