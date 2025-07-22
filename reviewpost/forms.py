# forms.py
from django import forms
from .models import ReviewModel

class ReviewForm(forms.ModelForm):
    class Meta:
        model = ReviewModel
        fields = ['title', 'content', 'images', 'evaluation']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'images': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'evaluation': forms.Select(attrs={'class': 'form-select'}),
        }
