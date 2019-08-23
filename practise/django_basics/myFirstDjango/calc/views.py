from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    #return HttpResponse("<h1>HelloWorld</h1>")
    #if you need simple template
    #return render(request, 'home.html')
    #if you need to pass values to template 
    return render(request, 'home.html',{'name':'Nani'})

def add(request):
    val1 = int(request.GET['num1'])
    val2 = int(request.GET['num2'])
    res = val1 + val2
    return render(request, 'result.html', {'res':res})

def addpost(request):
    val1 = int(request.POST['num1'])
    val2 = int(request.POST['num2'])
    res = val1 + val2
    return render(request, 'result.html', {'res':res})