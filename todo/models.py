# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from authentication.models import Account

# Create your models here.
class ToDoList(models.Model):
    user=models.ForeignKey(Account,on_delete=models.CASCADE)
    name = models.CharField(max_length=128)
    creation_date = models.DateField(auto_now_add=True)
    #
    # def __unicode__(self):
    #     return self.name

class ToDoItem(models.Model):
    descrip = models.TextField()
    completed = models.BooleanField(default=False)
    due_by = models.DateField()
    list=models.ForeignKey(ToDoList,on_delete=models.CASCADE)
    #
    # def __unicode__(self):
    #     return self.list