from .models import Image
from django import forms

class NewImageForm(forms.ModelForm):
    class Meta:
        model = Image
        exclude = ['url', 'comments','likes','name']
        widgets = {}
class CommentsForm(forms.Form):
    comment = forms.CharField(max_length=100)
