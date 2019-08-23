from django.shortcuts import render
from .models import Destination

# Create your views here.
def index123(request):

    dest1 = Destination()
    dest1.name = 'Mumbai'
    dest1.description = 'The city that never sleeps'
    dest1.img = 'destination_1.jpg'
    dest1.price = 802.124
    dest1.offer = False

    dest2 = Destination()
    dest2.name = 'Singapore'
    dest2.description = 'Asian Hub'
    dest2.img = 'destination_2.jpg'
    dest2.price = 811.124
    dest2.offer = False

    dest3 = Destination()
    dest3.name = 'Thailand'
    dest3.description = 'The most stunning eastern entertainment'
    dest3.img = 'destination_3.jpg'
    dest3.price = 522.124
    dest3.offer = True

    dests  = [dest1, dest2, dest3]

    #return render(request,'index.html',{'dest1': dest1, 'dest2': dest2, 'dest3' : dest3})
    return render(request,'index.html',{'dests': dests})

def index(request):
    #using database ORM 
    dests = Destination.objects.all()
    return render(request,'index.html',{'dests': dests})
