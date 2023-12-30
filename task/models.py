from django.db import models

# Create your models here.
# taskTitle 
# taskDescription 
# is_completed by default False
# Task Assign Date

class TaskModel(models.Model):
    task_title = models.CharField(max_length=20)
    task_description = models.CharField(max_length=100)
    is_completed = models.BooleanField(default=False)
    assign_date = models.DateField()