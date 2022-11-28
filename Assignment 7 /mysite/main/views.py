from urllib import request
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import ContactForm
from .models import Contact
from django.db.models import Q

# Create your views here.
def homepage(request):
  if request.method == "POST":
    form = ContactForm(request.POST)
    if form.is_valid():
      form.save()
  contacts = Contact.objects.all().order_by('name', 'profession').values()
  # contacts=contacts.sort(key=lambda x: x.name.lower())
  form = ContactForm()
  return render(request, "home.html", {"form": form, "contacts":contacts})


def update(request,a):
    
    contact= Contact.objects.get(id=a)
    form= ContactForm(instance=contact)
    
    
    if request.method =="POST":
      form= ContactForm(request.POST, instance=contact)
      if form.is_valid():
        form.save()
        return redirect('/')
    context ={'form':form}
    return render(request, 'home.html',context)


def delete(request,a):
	contact= Contact.objects.get(id=a)
	if request.method=='POST':
		contact.delete()
		return(redirect('/'))

	context ={'contact':contact}
	return render(request, "delete.html", context)

def sname(request):
  if request.method == "POST":
    name = request.POST.get('name')
    contacts= Contact.objects.filter(Q(name__contains=name) | Q(mobile_number__contains=name))
    return render(request, "search.html", { 'contacts':contacts})
  else:
    return render(request, "search.html", {})

def sprofession(request):
  if request.method == "POST":
    searched = request.POST.get('name')
    contacts= Contact.objects.filter(profession__contains=searched)
    return render(request, "search_profession.html", { 'contacts':contacts})
  else:
    return render(request, "search_profession.html", {})

def compare(request):
  if request.method == "POST":
    one = request.POST.get('compared')
    two = request.POST.get('comparedtwo')

    contacts= Contact.objects.filter(name__contains=one)
    contactstwo= Contact.objects.filter(name__contains=two)
    
    return render(request, "compare.html", { 'contacts':contacts, 'contactstwo':contactstwo})
  else:
    return render(request, "compare.html", {})
