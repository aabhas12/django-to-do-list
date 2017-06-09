from django import forms
from django.forms import Textarea
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from app.models import List,Task,Comment
from app import models

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')


    class Meta:
       model = User
       fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

class newlist(forms.ModelForm):

    class Meta:
        model=List
        fields=('name','assigned_to','due_date')
        exclude=('created_by',)

class newtask(forms.ModelForm):
    class Meta:
        model=Task
        fields=('title','assigned_to','due_date','note')

class newcomment(forms.ModelForm):

    class Meta:
        model=Comment
        fields=('body',)
        widgets = {
            'body': Textarea(attrs={ 'class':'form-control', 'rows': 3,'placeholder':'Enter Your Comment Here'}),
        }




