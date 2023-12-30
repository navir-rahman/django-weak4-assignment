from django.db import models
from task.models import TaskModel
# Create your models here.
# Category Name
# Many-to-Many Relationships with task model     

class CategoryModel(models.Model):
    category_name = models.CharField(max_length=20)
    task = models.ManyToManyField(TaskModel)