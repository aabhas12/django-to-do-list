from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from app.models import List
from app import models

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')


    class Meta:
       model = User
       fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

class newlist(forms.ModelForm):
    #Name=forms.CharField(max_length=20)
    #Priority=forms.ChoiceField(choices=models.PRIORITY_OPTIONS)
    #AssignTo=forms.ModelChoiceField(queryset=User.objects.all())
    #DueDate=forms.DateField()
    def __init__(self):
        super(newlist, self).__init__()
        self.fields['priority'].choices=models.PRIORITY_OPTIONS
    class Meta:
        model=List
        fields=('name','priority','assigned_to','due_date')


