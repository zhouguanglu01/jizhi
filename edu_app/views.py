from django.shortcuts import render, HttpResponse

# Create your views here.

def indexAdmin(request):
    return HttpResponse("app admin")
