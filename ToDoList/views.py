from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
from ToDoList import models
from django.http import HttpResponseRedirect
from django.contrib import messages

# Create your views here.
def index(request):
    todo_items = models.ToDo.objects.all().order_by('-added_date')
    return render(request, 'main/index.html', {"todo_items":todo_items})

@csrf_exempt
def add_todo(request):
    #print(request.POST)
    current_time = timezone.now()
    content = request.POST['content']
    todo = models.ToDo.objects.create(added_date=current_time, text=content)
    total_todo = models.ToDo.objects.all().count()

    if todo.pk:
        return HttpResponseRedirect("/", messages.success(request, "ToDo item created successfully."))
    else:
       return HttpResponseRedirect("/", messages.error(request, "ToDo cannot be deleted."))

@csrf_exempt
def delete_todo(request, todo_id):
    result = models.ToDo.objects.get(id=todo_id).delete()
    if result[0] > 0:
        return HttpResponseRedirect("/", messages.success(request, "ToDo deleted successfully."))
    else:
        return HttpResponseRedirect("/", messages.error(request, "ToDo cann't be deleted"))