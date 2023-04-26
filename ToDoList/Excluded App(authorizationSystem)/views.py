from django.shortcuts import render, redirect
from authorizationSystem.models import Licenses
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from authorizationSystem.forms import LicenseForm
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def login_view(request):
    if request.method == 'POST':
        #usernmae = request.post.get('username')
        username = request.POST['username']
        pswd = request.POST['pass']

        user = authenticate(username=username, password=pswd)
        #print()
        print('user--',user)

        if user is not None:
            login(request,user)
            return redirect('/index/')
        else:
            messages.error(request,'Wrong Credntials!')
            return redirect('/')

    return render(request,'authorizationSystem/login.html')

def signup_view(request):
    active_usr = len([usr for usr in User.objects.all() if usr.is_active])
    if request.method == 'POST':
        if active_usr < Licenses.objects.first().max_user:
            username = request.POST['username']
            fname = request.POST['firstname']
            lname = request.POST['lastname']
            email = request.POST['email']
            pass1 = request.POST['pass1']
            
            usr = User.objects.create_user(username,email,pass1)
            usr.first_name = fname
            usr.last_name = lname
            usr.save()
            count = User.objects.all().count()
            return redirect('/')
        else:
            return render(request,'authorizationSystem/signup.html',context = {'msg':'User Limit  Exceed'})
					
    return render(request,'authorizationSystem/signup.html')

def logout_view(request):
    logout(request)
    return redirect('/')

#@login_required
def index_view(request):
    if not request.user.is_authenticated:
        return redirect('/')
    name = request.user.first_name
    return render(request,'authorizationSystem/index.html',{'name':name})


def adminLogin_view(request):
    if request.method == 'POST':
        #usernmae = request.post.get('username')
        username = request.POST['username']
        pswd = request.POST['pass']

        user = authenticate(username=username, password=pswd)
        if user is not None:
            if not user.is_superuser:
                return redirect('/')
            login(request,user)
            return redirect('/view/')
        else:
            messages.error(request,'Wrong Credntials!')
            return redirect('/adminsLogin/')

    return render(request,'authorizationSystem/adminLogin.html')



def licenses_view(request):
    if not request.user.is_authenticated and request.user.is_superuser:
        return redirect('/adminsLogin/')
    lic = Licenses.objects.first()
    return render(request,'authorizationSystem/licenses.html',{'lic':lic})


def update_view(request,id):
    if not request.user.is_authenticated and request.user.is_superuser:
        return redirect('/adminsLogin/')
    lic = Licenses.objects.get(id = id)
    if request.method == "POST":
        form = LicenseForm(request.POST,instance=lic)
        print(form.errors)
        print(form.is_valid())
        if form.is_valid():
            form.save()
            return redirect('/view/')
    return render(request,'authorizationSystem/update.html',{'lic':lic})


    
