from .models import Image,Comment
from django import forms

class NewImageForm(forms.ModelForm):
    class Meta:
        model = Image
        exclude = ['url', 'comments','likes','name']
        widgets = {}
class CommentsForm(forms.ModelForm):
    class Meta:
        model=Comment
        fields=('commented_by','body','for_image')
