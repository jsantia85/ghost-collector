from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Ghost, Toy
from .forms import FeedingForm

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
  feeding_form = FeedingForm()
  return render(request, 'ghosts/detail.html', {
    'ghost': ghost, 'feeding_form': feeding_form
  })

class GhostCreate(CreateView):
  model = Ghost
  fields = '__all__'

class GhostUpdate(UpdateView):
  model = Ghost
  fields = ['species', 'description', 'age']

class GhostDelete(DeleteView):
  model = Ghost
  success_url = '/ghosts/'

def add_feeding(request, ghost_id):
  form = FeedingForm(request.POST)
  if form.is_valid():
    new_feeding = form.save(commit=False)
    new_feeding.ghost_id = ghost_id
    new_feeding.save()
  return redirect('ghosts_detail', ghost_id=ghost_id)

class ToyCreate(CreateView):
  model = Toy
  fields = '__all__'

class ToyList(ListView):
  model = Toy

class ToyDetail(DetailView):
  model = Toy

class ToyUpdate(UpdateView):
  model = Toy
  fields = ['name', 'color']

class ToyDelete(DeleteView):
  model = Toy
  success_url = '/toys/'