from django.shortcuts import render
from task.models import TaskModel
from category.models import CategoryModel
# Create your views here.
def home(request):
    data = TaskModel.objects.all()
    categories = CategoryModel.objects.all()
    return render(request, 'home.html', {'data': data, 'category': categories})
