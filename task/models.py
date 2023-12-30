from django.db import models 

class TaskModel(models.Model):
    task_title = models.CharField(max_length=20)
    task_description = models.CharField(max_length=100)
    is_completed = models.BooleanField(default=False)
    assign_date = models.DateTimeField()

    def __str__(self):
        return self.task_title