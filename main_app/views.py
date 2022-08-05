from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Ghost, Toy
from .forms import FeedingForm

# Create your views here.
class Home(LoginView):
  template_name = 'home.html'

def about(request):
  return render(request, 'about.html')

@login_required
def ghosts_index(request):
  ghosts = Ghost.objects.filter(user=request.user)
  return render(request, 'ghosts/index.html', { 'ghosts': ghosts })

@login_required
def ghosts_detail(request, ghost_id):
  ghost = Ghost.objects.get(id=ghost_id)
  toys_ghost_doesnt_have = Toy.objects.exclude(id__in = ghost.toys.all().values_list('id'))
  feeding_form = FeedingForm()
  return render(request, 'ghosts/detail.html', {
    'ghost': ghost, 'feeding_form': feeding_form, 'toys': toys_ghost_doesnt_have
  })

class GhostCreate(LoginRequiredMixin, CreateView):
  model = Ghost
  fields = ['name', 'species', 'description', 'age']

  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)

class GhostUpdate(LoginRequiredMixin, UpdateView):
  model = Ghost
  fields = ['species', 'description', 'age']

class GhostDelete(LoginRequiredMixin, DeleteView):
  model = Ghost
  success_url = '/ghosts/'

@login_required
def add_feeding(request, ghost_id):
  form = FeedingForm(request.POST)
  if form.is_valid():
    new_feeding = form.save(commit=False)
    new_feeding.ghost_id = ghost_id
    new_feeding.save()
  return redirect('ghosts_detail', ghost_id=ghost_id)

class ToyCreate(LoginRequiredMixin, CreateView):
  model = Toy
  fields = '__all__'

class ToyList(LoginRequiredMixin, ListView):
  model = Toy

class ToyDetail(LoginRequiredMixin, DetailView):
  model = Toy

class ToyUpdate(LoginRequiredMixin, UpdateView):
  model = Toy
  fields = ['name', 'color']

class ToyDelete(LoginRequiredMixin, DeleteView):
  model = Toy
  success_url = '/toys/'

@login_required
def assoc_toy(request, ghost_id, toy_id):
  Ghost.objects.get(id=ghost_id).toys.add(toy_id)
  return redirect('ghosts_detail', ghost_id=ghost_id)

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('ghosts_index')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'signup.html', context)