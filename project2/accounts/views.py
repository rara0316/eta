from django.shortcuts import render
# from .forms import UserForm, LoginForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.http import HttpResponse
from django.contrib import auth

# Create your views here.
def index(request):
    return render(request, 'index.html')


def signup(request):
    if request.method != 'POST':
        form = UserCreationForm()
    else:
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            new_user = form.save()
            authenticated_user = authenticate(username=new_user.username,
                                              password=request.POST['password1'])
            login(request, authenticated_user)
            return HttpResponseRedirect(reverse('index'))

    context = {'form': form}
    return render(request, 'signup.html', context)


def login_view(request):  #메소드 이름 login으로하면 오류날 수 있음
    if request.user.is_authenticated:
        return HttpResponseRedirect('/accounts')
    if request.method == 'GET':
        form = AuthenticationForm()
        return render(request, 'login.html', {'form': form})
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                print(user)
                login(request, user)
                return HttpResponseRedirect('/accounts')
            else:
                print('User not found')
        else:
            return render(request, 'login.html', {'form': form})
        

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('index'))