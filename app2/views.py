from django.shortcuts import render


# Create your views here.
from django.http import HttpResponse
def abd(request):
    return HttpResponse('<h1>abd is best alrounder</h1>')

def raina(request):
     return HttpResponse('<h1>raina is mister IPL</h1>')

