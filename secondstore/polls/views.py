from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('Heya cowgirls and cowbows! \
                         This is the polls index, boy howdy!')

def secret(request):
    return HttpResponse("Now this is just fun to add, no?")