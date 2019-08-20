from django.shortcuts import render, HttpResponse

# Create your views here.
# import  configparser
#
# conf = configparser.ConfigParser()
# conf.read('web.conf')
from edu_web.web import  *
def indexAdmin(request):
    dict_send = globals().copy()
    return render(request, "web/index.html",dict_send)

def error(request):
    return render(request,"web/error.html",status=404)
