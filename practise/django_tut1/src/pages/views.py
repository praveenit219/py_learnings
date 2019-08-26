from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def home_view(request, *args, **kwargs):
    print(args, kwargs)
    print(request.user) #can see wahts coming with request
    #return HttpResponse("<h1> Hello World! </h1>")
    return render(request, 'home.html', {})

def contact_view(request, *args, **kwargs):
    #return HttpResponse("<h1> contact page! </h1>")
     return render(request, 'contact.html', {})

def about_view(request, *args, **kwargs):

    mycontext = {
        'my_text': 'This is about us',
        'my_number': 1234,
        'my_list': [23,"sdfkh"]
    }

    #return HttpResponse("<h1> About page! </h1>")
    return render(request, 'about.html', mycontext)