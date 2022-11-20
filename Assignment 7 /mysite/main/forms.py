from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import ModelForm
from django import forms
from .models import *
from .models import Contact

class ContactForm(forms.ModelForm):

  class Meta:
    model = Contact
    fields = '__all__'