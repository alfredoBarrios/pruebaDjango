from django.shortcuts import render
from django.http import HttpResponse

def inicio(request):
    return render(request,'inicio.html',{})



from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    return HttpResponse('Home Page')