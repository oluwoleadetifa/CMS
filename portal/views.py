from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect

# Create your views here.
from django.views import View


def IndexView(request):
    return render(request, 'portal/index.html')


def Login(request):
    form = AuthenticationForm()
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('portal.index')
        else:
            messages.info(request, "Username or password is incorrect")
    return render(request=request, template_name='portal/login.html', context={'form': form})


def logoutUser(request):
    logout(request)
    return redirect('portal.login')

