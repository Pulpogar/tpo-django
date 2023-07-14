from django.shortcuts import render

# Create your views here.
def contact(request):
    return render(request, "core/contact.html")


def genders(request):
    return render(request, "core/genders.html")


def index(request):
    return render(request, "core/index.html")


def reviews(request):
    return render(request, "core/reviews.html")


def search(request):
    return render(request, "core/search.html")


