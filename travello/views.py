from django.shortcuts import render
from .models import Destination

def index(request):
    dest1 = Destination(1,'Bangalore','Traffic first, beauty next','destination_1.jpg',700,True)
    dest2 = Destination(2,'Hyderabad','First biryani then, Sherwani','destination_2.jpg',650,False)
    dest3 = Destination(3,'Mumbai','India\'s crowdest city','destination_3.jpg',800,False)
    dests = [dest1,dest2,dest3]
    return render(request, 'index.html',context={'dests':dests})