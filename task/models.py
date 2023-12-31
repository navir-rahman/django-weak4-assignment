from django.db import models 
from category.models import CategoryModel
class TaskModel(models.Model):
    task_title = models.CharField(max_length=20)
    task_description = models.CharField(max_length=100)
    is_completed = models.BooleanField(default=False)
    category = models.ManyToManyField(CategoryModel)
    
    assign_date = models.DateTimeField()

    def __str__(self):
        return self.task_title