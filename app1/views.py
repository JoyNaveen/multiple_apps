from django.shortcuts import render


# Create your views here.
from django.http import HttpResponse
def dhoni(request):
    return HttpResponse('<h1>dhoni is best finisher</h1>')

def virat(request):
     return HttpResponse('<h1>virat is scored most runs</h1>')
