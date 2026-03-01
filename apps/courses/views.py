from django.shortcuts import render

def home_view(request):
    return render(request, "courses/home.html")

def about_view(request):
    return render(request, "courses/about.html")