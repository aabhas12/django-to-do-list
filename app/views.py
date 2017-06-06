from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from app.forms import SignUpForm, newlist
from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm

from django.shortcuts import render, redirect
def index(request):
    """
        Renders frontend homepage
    """
    data = {'title': 'Welcome - To Do Application'}
    return render(request, 'index.html', data)

def lists(request):
    return render(request, 'lists.html',{})

def log_out(request):
    logout(request)
    return redirect('index')
def create(request):
    if request.POST=='POST':
       pass
    else:
       form1= newlist()
       data=User.objects.all()

    return render(request,'create.html',{'form1':form1,'data':data})
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('lists')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})