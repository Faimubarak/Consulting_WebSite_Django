from django.shortcuts import render , redirect

from django.views.generic import ListView , DetailView
from .models import Counslat ,Comment
from .filters import FliterCounslat
from .froms import Reviews , Counslating
from accounts.models import Profile
from django.urls import reverse
from django.core.paginator import Paginator
# Create your views here.
#view all coulisting from database and take the queryset to django fliters to fliter resulat
def consulatlist(request):
    object_list = Counslat.objects.all()
    fliter = FliterCounslat(request.GET,Counslat.objects.all())
    paginator = Paginator(object_list, 10) 
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'object_list':page_obj,'myfilter':fliter}
    return render(request,'consulat/counslat_list.html',context)

# view one comsulat by id and add comments 
def consulatdetail(request,id):
    consulat = Counslat.objects.get(id=id)
    review = Comment.objects.filter(counslat=consulat)
    user_info = Profile.objects.get(user=consulat.user)
    form = Reviews()
    if request.method == 'POST':
        form = Reviews(request.POST)
        if form.is_valid():
            my_form = form.save(commit=False)
            my_form.counslat = consulat
            my_form.user = request.user
            my_form.save()
    context = {'consulat':consulat,'review':review,'form':form,'info':user_info}
    return render(request,'consulat/detail.html',context)


# add counslat to database
def add_counslating(request):
    form = Counslating()
    if request.method == 'POST':
        form = Counslating(request.POST)
        if form.is_valid():
            my_form = form.save(commit=False)
            my_form.user = request.user
            my_form.save()
            return redirect(reverse('consulat:consulat_list'))
    return render(request,'consulat/add_counslat.html',{'form':form})