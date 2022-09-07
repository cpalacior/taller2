from re import search
from django.shortcuts import render
from django.http import HttpResponse
from .models import Movie
# Create your views here.

def home(request):
    #return HttpResponse("<h1>Welcome to the home page</h1>")
    searchTerm = request.GET.get('searchMovie')
    if searchTerm:
        movies = Movie.objects.filter(title__icontains=searchTerm)
    else:
        movies = Movie.objects.all()
    
    return render(request, 'home.html', {'objetoBuscado': searchTerm, 'peliculas': movies})