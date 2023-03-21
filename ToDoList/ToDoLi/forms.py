from django import forms
from ToDoLi.models import Task

class TaskForm(forms.ModelForm):
	class Meta:
		model = Task
		fields = '__all__'
		widgets={
			'tname' : forms.TextInput(attrs={'placeholder':''})
		}
		'''widgets={
			'tname' : forms.TextInput(attrs={'class':'cssclass'})
		}'''
		