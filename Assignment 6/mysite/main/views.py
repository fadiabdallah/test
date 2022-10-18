from django.shortcuts import render
from .forms import TeamForm
from .models import Team

# Create your views here.
def homepage(request):
  if request.method == "POST":
    form = TeamForm(request.POST)
    if form.is_valid():
      form.save()
  teams = Team.objects.all()
  form = TeamForm()
  return render(request, "home.html", {"form": form, "teams":teams}) 