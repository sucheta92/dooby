from django.db import models
from django import forms

class Posting(models.Model):
    writing = models.CharField(max_length=300)
    user = models.CharField(max_length=200)

class likes(models.Model):
    vote = models.ForeignKey(Posting)
    like = models.IntegerField(default=0)

class Blog(forms.Form):
    text=forms.CharField(max_length=1000,widget=forms.Textarea)
    header=forms.CharField(max_length=300)
