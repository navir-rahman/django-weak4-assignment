from django.shortcuts import render
from task.models import TaskModel
from category.models import CategoryModel

def home(request):
    task = TaskModel.objects.all()

    # categories = CategoryModel.objects.all()

    return render(request, 'home.html', {'tasks': task})
