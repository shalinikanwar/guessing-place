from django import forms
from .models import HomePageImage,Comments
class ItemForm(forms.ModelForm):
    class Meta:
        model=HomePageImage
        fields=['image','location']
class CommentsForm(forms.ModelForm):
    class Meta:
        model=Comments
        fields=['comments']
