from django.shortcuts import render
from consulat.models import Catgory
# Create your views here.

#The home page view to return the categorys on serivce section
def home(request):
    service = Catgory.objects.all()
    return render(request,'home/home.html',{'service':service})