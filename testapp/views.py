from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def good_morning_view(request):
    return HttpResponse('<h1> good morning friends</h1>')

def good_evening_view(request):
    return HttpResponse('<h1> good evening friens </h1>')