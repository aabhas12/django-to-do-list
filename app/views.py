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
    if request.method=='POST':
       form1=newlist(request.POST)
       print ("we are here")
       if form1.is_valid():
           print(form1)
           print(form1.cleaned_data.get('Priority'))
           form1.save()

           return redirect('index.html')

    else:
       form1= newlist()

    return render(request,'create.html',{'form1':form1})
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():

            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('index')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})