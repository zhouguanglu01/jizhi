from django.shortcuts import render, HttpResponse

# Create your views here.

def indexAdmin(request):
    # return HttpResponse("web admin")
    return render(request, "web/index.html")
