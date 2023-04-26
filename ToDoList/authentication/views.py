from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login
# Create your views here.
def login_view(request):
    if request.method == 'POST':
        #usernmae = request.post.get('username')
        username = request.POST['username']
        pswd = request.POST['pass']

        user = authenticate(username=username, password=pswd)
        print(user_can_authenticate())

        if user is not None:
            login(request,user)
            return redirect('/ToDoList/')
        else:
            messages.error(request,'Wrong Credntials!')
            return redirect('/login')

    return render(request,'authentication/login.html')

def signup(request):
    if request.method == 'POST':
        #usernmae = request.post.get('username')
        username = request.POST['username']
        fname = request.POST['firstname']
        lname = request.POST['lastname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        myuser = User.objects.create_user(username,email,pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()

        messages.success(request,"Account created Successfully")

        return redirect('/login')

    return render(request,'authentication/signup.html')
