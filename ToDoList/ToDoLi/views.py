from django.shortcuts import render,redirect
from ToDoLi.models import Task
from ToDoLi.models import CompletedTask
from ToDoLi.forms import TaskForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
# Create your views here.

#@login_required
def display_Tasks(request):

	if not request.user.is_authenticated:
		return redirect('/login')

	cur_user = request.user.id
	tsk = Task.objects.all().filter(tuser=cur_user)
	return render(request,'ToDoLi/index.html',{'task':tsk})
	
def create_view(request):
	if not request.user.is_authenticated:
		return redirect('/login')
	#print('reqid_val',request.user.id)
	tsk = TaskForm()
	if request.method=="POST":
		form = TaskForm(request.POST)
		if form.is_valid():
			tsk = Task.objects.create(tname = request.POST['tname'],tDetails = request.POST['tDetails'],tuser = request.user.id)
			#print('---->',tsk)
			return redirect('/ToDoList/')
	return render(request,'ToDoLi/create.html',{'form':tsk})
		
	
def update_view(request,id):
	if not request.user.is_authenticated:
		return redirect('/login')
	tsk = Task.objects.get(id=id)
	if request.method == "POST":
		form = TaskForm(request.POST,instance = tsk)
		if form.is_valid():
			form.save()
			return redirect('/ToDoList/')
	return render(request,'ToDoLi/update.html',{'task':tsk})

def delete_view(request,id):
	if not request.user.is_authenticated:
		return redirect('/login')
	try:
		ctsk = CompletedTask.objects.get(id=id)
		if ctsk:
			ctsk.delete()
			return redirect('/ToDoList/completed')
	except CompletedTask.DoesNotExist:
		tsk = Task.objects.get(id=id)
		tsk.delete()
	return redirect('/ToDoList/')
	
def markdone_view(request,id):
	if not request.user.is_authenticated:
		return redirect('/login')
	tsk = Task.objects.get(id=id)
	ctsk = CompletedTask.objects.create(ctname = tsk.tname,ctDetails = tsk.tDetails,ctuser = request.user.id )
	tsk.delete()
	return redirect('/ToDoList/')

def completed(request):
	if not request.user.is_authenticated:
		return redirect('/login')
	ctsk = CompletedTask.objects.all()
	return render(request,'ToDoLi/completed.html',{'ctask':ctsk})

def details(request,id):
	if not request.user.is_authenticated:
		return redirect('/login')
	tsk = Task.objects.get(id=id)
	return render(request,'ToDoLi/details.html',{'task':tsk})

def detail_update(request,id):
	if not request.user.is_authenticated:
		return redirect('/login')
	tsk = Task.objects.get(id=id)
	if request.method == "POST":
		form = TaskForm(request.POST,instance = tsk)
		if form.is_valid():
			form.save()
			return redirect('/ToDoList/')
	return render(request,'ToDoLi/update.html',{'task':tsk,'Condition':True})

def login_view(request):
	return render(request,'ToDoLi/login.html',{})

def logout_view(request):
	logout(request)
	return redirect('/login')
