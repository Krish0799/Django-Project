from django.contrib.auth.middleware import RemoteUserMiddleware
from django.contrib.sessions.models import Session
from django.utils import timezone
from django.http import HttpResponse
from django.shortcuts import render, redirect
from authorizationSystem.models import Licenses

class LoginsMiddleware(RemoteUserMiddleware):
    def process_request(self, request):
        super().process_request(request)
        if request.user.is_authenticated:
            # Get the number of active sessions for the user
            session_count = Session.objects.filter(
                expire_date__gte=timezone.now()).count()
            # Check if the user has reached the maximum number of concurrent logins
            license = Licenses.objects.first()
            if session_count > license.max_active:
                request.session.flush()
                return render(request,'authorizationSystem/login.html',{'msg':'Login Limit Exceeded'})
                #return HttpResponse('You have reached the maximum number of concurrent logins.')