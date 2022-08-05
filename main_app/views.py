from django.shortcuts import render
from .models import Ghost

# Create your views here.
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def ghosts_index(request):
  ghosts = Ghost.objects.all()
  return render(request, 'ghosts/index.html', { 'ghosts': ghosts })

def ghosts_detail(request, ghost_id):
  ghost = Ghost.objects.get(id=ghost_id)
  return render(request, 'ghosts/detail.html', { 'ghost': ghost })

