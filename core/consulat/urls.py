from django.urls import path
from .views import consulatlist , consulatdetail
app_name = 'consulat'
urlpatterns = [
    path('list',consulatlist,name='consulat_list'),  
    path('list/<int:id>',consulatdetail,name='detail'),
]