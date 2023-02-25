from django.shortcuts import render
from django.views.generic import ListView , DetailView
from .models import Counslat ,Comment
# Create your views here.
class consulat_List(ListView):
    model = Counslat 


def consulatdetail(request,id):
    consulat = Counslat.objects.get(id=id)
    review = Comment.objects.filter(counslat=consulat)

    return render(request,'consulat/detail.html',{consulat:'consulat',review:'review'})