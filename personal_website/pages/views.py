from django.shortcuts import render
from django.http import HttpResponse


def home_page_view(request):
    return HttpResponse("Welcome to the Home Page!")


def about_page_view(request):
    context = {"name": "Alice", "age": 30}
    return render(request, "pages/about.html", context)
