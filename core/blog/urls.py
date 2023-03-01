from django.urls import path
from .views import blog_list , blog_detil
app_name = 'blog'
urlpatterns = [
    path('',blog_list,name='blog'),
    path('\<int:id>',blog_detil,name='detail'),
]