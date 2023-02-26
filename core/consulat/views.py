from django.shortcuts import render

from django.views.generic import ListView , DetailView
from .models import Counslat ,Comment
from .filters import FliterCounslat
from .froms import Reviews
# Create your views here.
'''
[comments]
--> proflie.details[consulatdetail]...
add consulat --- from --- botstrap4
'''
def consulatlist(request):
    object_list = Counslat.objects.all()
    fliter = FliterCounslat(request.GET,object_list)
    context = {'object_list':object_list,'filter':fliter}
    return render(request,'consulat/counslat_list.html',context)

def consulatdetail(request,id):
    consulat = Counslat.objects.get(id=id)
    review = Comment.objects.filter(counslat=consulat)
    form = Reviews()
    if request.method == 'POST':
        form = Reviews(request.POST)
        if form.is_valid():
            my_form = form.save(commit=False)
            my_form.counslat = consulat
            my_form.user = request.user
            my_form.save()
    context = {'consulat':consulat,'review':review,'form':form}
    return render(request,'consulat/detail.html',context)