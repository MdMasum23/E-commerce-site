from django import forms
from .models import Category, Tag

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = "__all__"

class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = "__all__"