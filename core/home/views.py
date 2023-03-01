from django.shortcuts import render
from consulat.models import Catgory
# Create your views here.
def home(request):
    service = Catgory.objects.all()
    return render(request,'home/home.html',{'service':service})