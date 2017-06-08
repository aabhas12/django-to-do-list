from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect,get_object_or_404

from django.contrib.auth.models import User
from app.forms import SignUpForm, newlist
from django.contrib.auth import logout
from app.models import List
from app import models
from django.contrib.auth.forms import UserCreationForm

from django.shortcuts import render, redirect
def index(request):
    """
        Renders frontend homepage
    """
    data = {'title': 'Welcome - To Do Application'}
    return render(request, 'index.html', data)

def lists(request):
    Lists=List.objects.all()

    return render(request, 'lists.html',{'Lists':Lists,'data':models.PRIORITY_OPTIONS1})

def log_out(request):
    logout(request)
    return redirect('index')
def create(request):
    if request.method=='POST':
       form1=newlist(request.POST)
       print ("we are here")
       if form1.is_valid():
          abc=form1.save(commit=False)
          abc.created_by=request.user

          abc.priority=request.POST['Priority']

          #print()
           # #form1['created_by']=
           # form1.cleaned_data.get('prior')
          abc.save()

          return redirect('list')

    else:
       form1= newlist()

    return render(request,'create.html',{'form1':form1})
def viewlist(request,id):
    # if request.method=='POST':
    #    form1=newlist(request.POST)
    #    print ("we are here")
    #    if form1.is_valid():
    #       abc=form1.save(commit=False)
    #       abc.created_by=request.user
    #       abc.priority=form1.cleaned_data.get('Priority')
    #
    #       #print()
    #        # #form1['created_by']=
    #        # form1.cleaned_data.get('prior')
    #       abc.save()
    #
    #       return redirect('list')
    #
    # else:
    Listbyid=get_object_or_404(List,id=id)
    print("we are here")
    #print(Lists.name)
    #print(Lists.created_by)
    form1= newlist()
    #print(id)

    return render(request,'viewlists.html',{'Lists':Listbyid})

def deletelist(request,id):
    server = get_object_or_404(List, id=id)
    server.delete()
    return redirect('list')
def editlist(request,id):

    Listbyid = get_object_or_404(List,id=id)
    if request.method=="POST":
       form1=newlist(request.POST,instance=Listbyid)
       if form1.is_valid():
           abc = form1.save(commit=False)
           abc.created_by = request.user
           abc.priority = request.POST['Priority']
           abc.save()
           return redirect('list')
    else:
        pnum=Listbyid.priority
        form1= newlist(instance=Listbyid)
        print(pnum)
    return render(request,'editlist.html',{'form':form1,'pnum':pnum})
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