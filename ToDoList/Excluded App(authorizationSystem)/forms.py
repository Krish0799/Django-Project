from django import forms
from authorizationSystem.models import Licenses

class LicenseForm(forms.ModelForm):
	class Meta:
		model = Licenses
		exclude=[]
		'''widgets={
			'max_user' : forms.TextInput(attrs={'class':''})
		}'''
		