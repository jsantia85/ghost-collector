from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
  return HttpResponse('<h1>Hello ᓚᘏᗢ</h1>')

def about(request):
  return render(request, 'about.html')

class Ghost:
  def __init__(self, name, species, description, age):
    self.name = name
    self.species = species
    self.description = description
    self.age = age

ghosts = [
  Ghost('Lolo', 'tabby', 'Kinda rude.', 3),
  Ghost('Sachi', 'tortoiseshell', 'Looks like a turtle.', 0),
  Ghost('Fancy', 'bombay', 'Happy fluff ball.', 4),
  Ghost('Bonk', 'selkirk rex', 'Meows loudly.', 6)
]

def ghosts_index(request):
  return render(request, 'ghosts/index.html', { 'ghosts': ghosts })