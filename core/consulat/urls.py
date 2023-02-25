from django.urls import path
from .views import consulat_List , consulatdetail
app_name = 'consulat'
urlpatterns = [
    path('list',consulat_List.as_view(),name='consulat_list'),  
    path('list/<int:id>',consulatdetail,name='detail'),
]