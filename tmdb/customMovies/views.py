from django.shortcuts import render
from .models import Movie

# Create your views here.
def customs(request):
    movies = Movie.objects.all()
    return render(request, "customMovies/customs.html", {'movies':movies})