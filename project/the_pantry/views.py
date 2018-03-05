from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

#===========================================#
#           OTHER USER PROFILES             #
#===========================================#

# The index page is the login page. Once logged in, it takes you to home
def index(request):
    context_dict = {}
    return render(request, 'the_pantry/index.html', context = context_dict)

# Home page (for users who are logged in)
def home(request):
    context_dict = {}
    return render(request, 'the_pantry/home.html', context = context_dict)

# Trending page
def trending(request):
    context_dict = {}
    return render(request, 'the_pantry/trending.html', context = context_dict)

# Categories page
def categories(request):
    context_dict = {}
    return render(request, 'the_pantry/categories.html', context = context_dict)

# Favourites page
def favourites(request):
    context_dict = {}
    return render(request, 'the_pantry/favourites.html', context = context_dict)

# Profile page
def profile(request):
    context_dict = {}
    return render(request, 'the_pantry/profile.html', context = context_dict)

# Latest page
def latest(request):
    context_dict = {}
    return render(request, 'the_pantry/latest.html', context = context_dict)

# About page
def about(request):
    context_dict = {}
    return render(request, 'the_pantry/about.html', context = context_dict)

# Contact page
def contact(request):
    context_dict = {}
    return render(request, 'the_pantry/contact.html', context = context_dict)

# FAQ page
def faq(request):
    context_dict = {}
    return render(request, 'the_pantry/faq.html', context = context_dict)
