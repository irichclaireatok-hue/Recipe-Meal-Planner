from django import forms
from .models import Meal

class MealForm(forms.ModelForm):
    class Meta:
        model = Meal
        fields = ['day', 'meal_name', 'description', 'is_completed']
        widgets = {
            'day': forms.Select(attrs={
                'class': 'form-control',
                'placeholder': 'Select day'
            }),
            'meal_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter meal name',
                'required': True
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Enter meal description',
                'rows': 4
            }),
            'is_completed': forms.CheckboxInput(attrs={
                'class': 'form-check-input'
            })
        }
