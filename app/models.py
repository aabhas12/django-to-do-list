from django.db import models
from django.contrib.auth.models import User

PRIORITY_OPTION_LOW=3
PRIORITY_OPTION_MEDIUM=2
PRIORITY_OPTION_HIGH=1

PRIORITY_OPTIONS=((PRIORITY_OPTION_HIGH,'HIGH'),(PRIORITY_OPTION_MEDIUM,'MEDIUM'),(PRIORITY_OPTION_LOW,'LOW'))
PRIORITY_OPTIONS1={PRIORITY_OPTION_HIGH:'High',PRIORITY_OPTION_MEDIUM:'Medium',PRIORITY_OPTION_LOW:'Low'}

# The model List
class List(models.Model):
    name=models.CharField(max_length=50,verbose_name="*Name",help_text="Enter the name of the List")
    priority=models.IntegerField(verbose_name="*Priority")
    created_by=models.ForeignKey(User,related_name='list_created_by')
    assigned_to=models.ForeignKey(User,related_name='list_assigned_to')
    due_date=models.DateField(verbose_name="*Due Date")

    class Meta:
        db_table = "List"
#Task Model
class Task(models.Model):
    title=models.CharField(max_length=50)
    list=models.ForeignKey('List',on_delete=models.CASCADE)
    created_date=models.DateField()
    due_date = models.DateField()
    completed=models.BooleanField(default=False)
    completed_date=models.DateField(null=True)
    created_by=models.ForeignKey(User,related_name='task_created_by')
    assigned_to=models.ForeignKey(User,related_name='task_assigned_to')
    note=models.TextField(null=True)
    priority = models.IntegerField()


    class Meta:
        db_table = "Task"

#The Comment Model
class Comment(models.Model):
    author=models.ForeignKey(User)
    task=models.ForeignKey('Task',on_delete=models.CASCADE)
    date=models.DateTimeField()
    body=models.TextField()

    class Meta:
        db_table="Comment"

