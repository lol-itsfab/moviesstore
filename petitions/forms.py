from django import forms
from .models import Petition

class PetitionForm(forms.ModelForm):
    class Meta:
        model = Petition
        fields = ['title', 'description', 'movie_title']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter petition title'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Describe why this movie should be added to the catalog'}),
            'movie_title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter the movie title you want to petition for'}),
        }
