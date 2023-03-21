from django.contrib import admin
from ToDoLi.models import Task
from ToDoLi.models import CompletedTask

# Register your models here.
class TaskAdmin(admin.ModelAdmin):
	list = ['tname','tDetails']
	
class CompletedTaskAdmin(admin.ModelAdmin):
	list = ['ctname','ctDetails']
	
admin.site.register(Task,TaskAdmin)
admin.site.register(CompletedTask,CompletedTaskAdmin)