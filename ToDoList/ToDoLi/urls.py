"""ToDoList URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from ToDoLi import views

urlpatterns = [
	path('', views.display_Tasks),
	path('update/<id>',views.update_view),
	path('markdone/<id>',views.markdone_view),
	path('create/',views.create_view),
	path('delete/<id>',views.delete_view),
    path('completed/',views.completed),
    path('details/<id>',views.details),
    path('detail_update/<id>',views.detail_update),
    path('login/',views.login_view),
    path('logout/',views.logout_view),
	
	
]
