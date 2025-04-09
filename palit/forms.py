from django import forms
from .models import ColorScheme

class ColorSchemeForm(forms.ModelForm):
    class Meta:
        model = ColorScheme
        fields = ['name', 'background', 'menu', 'menu_text', 'text']