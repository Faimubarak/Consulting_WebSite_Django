from django.forms import ModelForm 
from .models import Comment , Counslat
class Reviews(ModelForm):
    class Meta:
        model = Comment
        fields = ['comment']


class Counslating(ModelForm):
    class Meta:
        model = Counslat
        fields = ['name','description','catgoray']