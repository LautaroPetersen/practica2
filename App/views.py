from django.shortcuts import render

# Create your views here.
def inicio(request):
    return render(request, "App/inicio.html")
def about(request):
    return render(request, "App/about.html")
def projects(request):
    return render(request, "App/projects.html")
def signup(request):
    return render(request, "App/signup.html")
