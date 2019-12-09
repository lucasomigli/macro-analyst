from django.http import HttpResponse
from django.shortcuts import render


def main(request):
    return render(request, 'main.html')


def home(request):
    return render(request, 'main.html')


def about(request):
    return render(request, 'about.html')
