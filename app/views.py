from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect,get_object_or_404

from django.contrib.auth.models import User
from app.forms import SignUpForm, newlist,newtask,newcomment
from django.contrib.auth import logout
from app.models import List,Task,Comment
from django.db.models import Count
from app import models
import time
import datetime
from django.contrib.auth.forms import UserCreationForm

from django.shortcuts import render, redirect
def index(request):
    """
        Renders frontend homepage
    """
    data = {'title': 'Welcome - To Do Application'}
    return render(request, 'index.html', data)

def lists(request):
    Lists=List.objects.all().order_by('priority')
    a={}
    b={}
    for i in Lists:
        taskbylistid = Task.objects.filter(list=i.id)

        completed = taskbylistid.filter(completed=True)
        a[i.id]=completed.__len__()
        incomplete = taskbylistid.filter(completed=False)
        b[i.id]=incomplete.__len__()


    return render(request, 'lists.html',{'Lists':Lists,'data':models.PRIORITY_OPTIONS1,'a':a,'b':b})

def log_out(request):
    logout(request)
    return render(request,'logout.html',{})

def martaskincomplete(request,id):
    taskbyid = get_object_or_404(Task, id=id)

    taskbyid.completed=False

    taskbyid.save()
    #print(Listbyid.completed)

    return redirect('viewlist' ,taskbyid.list.id)

def martaskcomplete(request,id):
    Taskbyid = get_object_or_404(Task, id=id)
    Taskbyid.completed=True
    Taskbyid.completed_date=datetime.datetime.now().date()
    Taskbyid.save()
    #print(Listbyid.completed)

    return redirect('viewlist' ,Taskbyid.list.id)

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
def createcomment(request,id):
    Taskbyid = get_object_or_404(Task, id=id)

    if request.method=='POST':
       form1=newcomment(request.POST)
       if form1.is_valid():
          abc=form1.save(commit=False)
          abc.author=request.user
          abc.task=Taskbyid
          abc.date=  datetime.datetime.now()
          abc.save()
          return redirect('view1task',id )

    else:
        form1= newcomment()
        print(Taskbyid.list.id)

    return render(request,'add_comment.html',{'form1':form1,'task':Taskbyid})
def createtask(request,id):
    Listbyid = get_object_or_404(List, id=id)
    if request.method=='POST':
        form1=newtask(request.POST)
        if form1.is_valid():
            abc=form1.save(commit=False)
            abc.priority = request.POST['Priority']
            abc.created_by = request.user
            abc.list=Listbyid
            #abc.completed=False
            abc.created_date=datetime.datetime.now().date()

            print(datetime.datetime.now().date())
            abc.save()

        return redirect('viewlist',id)

    else:
        form1= newtask()

    return render(request,'add_task.html',{'form1':form1,'list':Listbyid})
def view1task(request,id):
    taskbyid=get_object_or_404(Task,id=id)
    listbyid=get_object_or_404(List,id=taskbyid.list.id)
    comment=Comment.objects.filter(task=id)
    if request.method=='POST':
       print("i am here")
       form1=newcomment(request.POST)
       if form1.is_valid():

          abc=form1.save(commit=False)
          abc.author=request.user
          abc.task=taskbyid
          abc.date= datetime.datetime.now()
          abc.save()
          return redirect('view1task',id )

    else:
        form1=newcomment()
    return render(request,'viewtask.html',{'form1':form1,'lists':listbyid,'task':taskbyid,'data':models.PRIORITY_OPTIONS1,'comment':comment})


def viewlist(request,id):
    taskbylistid=Task.objects.filter(list=id)
    #taskbylistid=get_object_or_404(Task,list=id)
    print(taskbylistid)
    Listbyid=get_object_or_404(List,id=id)
    completed=taskbylistid.filter(completed=True)
    print(completed.__len__())
    incomplete=taskbylistid.filter(completed=False)
    print(incomplete.__len__())

    return render(request,'viewlists.html',{'Lists':Listbyid,'taskbylid':taskbylistid,'complete':completed.__len__(),'incomplete':incomplete.__len__(),'data':models.PRIORITY_OPTIONS1})

def deletelist(request,id):
    server = get_object_or_404(List, id=id)
    server.delete()
    return redirect('list')
def deletetask(request,id):
    server = get_object_or_404(Task, id=id)
    server.delete()
    return redirect('viewlist',server.list.id)
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
def edittask(request,id):

    Taskbyid = get_object_or_404(Task,id=id)
    #Listbyid = get_object_or_404(List, id=id1)
    if request.method=="POST":
        print("dfadf")
        form1=newtask(request.POST,instance=Taskbyid)
        if form1.is_valid():
            abc = form1.save(commit=False)

            abc.priority = request.POST['Priority']
            print(abc.priority)
            abc.save()
            return redirect('viewlist', Taskbyid.list.id)
    else:
        pnum=Taskbyid.priority
        form1= newtask(instance=Taskbyid)
        print(form1)
        print(pnum)
        return render(request,'edit_task.html',{'form1':form1,'pnum':pnum,'list':Taskbyid.list})
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