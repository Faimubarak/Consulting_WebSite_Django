from django.forms import ModelForm 
from .models import Comment
class Reviews(ModelForm):
    class Meta:
        model = Comment
        fields = ['comment']