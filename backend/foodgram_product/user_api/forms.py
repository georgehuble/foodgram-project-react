from django import forms
from .models import Teg, Ingredient, Recipe


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ("name", "author", "teg")
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control border"}),
            "author": forms.EmailInput(attrs={"class": "form-control border"}),
            "teg": forms.Textarea(attrs={"class": "form-control border"})
        }
        exclude = ['unit']
