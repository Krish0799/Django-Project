from django.shortcuts import render,redirect
from ToDoLi.models import Task
from ToDoLi.models import CompletedTask
from ToDoLi.forms import TaskForm

# Create your views here.

def display_Tasks(request):
	tsk = Task.objects.all()
	ctsk = CompletedTask.objects.all()
	return render(request,'ToDoLi/index.html',{'task':tsk,'ctask':ctsk})
	
def create_view(request):
	tsk = TaskForm()
	if request.method=="POST":
		form = TaskForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/')
	return render(request,'ToDoLi/create.html',{'form':tsk})
		
	
def update_view(request,id):
	tsk = Task.objects.get(id=id)
	if request.method == "POST":
		form = TaskForm(request.POST,instance = tsk)
		if form.is_valid():
			form.save()
			return redirect('/')
	return render(request,'ToDoLi/update.html',{'task':tsk})

def delete_view(request,id):
	ctsk = CompletedTask.objects.get(id=id)
	ctsk.delete()
	return redirect('/')
	
def markdone_view(request,id):
	tsk = Task.objects.get(id=id)
	ctsk = CompletedTask.objects.create(ctname = tsk.tname,ctDetails = tsk.tDetails)
	ctsk.save()
	tsk.delete()
	return redirect('/')