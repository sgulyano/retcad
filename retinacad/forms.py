from django import forms

from .models import FundusRetina

class FundusRetinaForm(forms.ModelForm):
    class Meta:
        model = FundusRetina
        fields = ['name', 'lefteye', 'righteye', 'taken_at']
        widgets = {
            'lefteye': forms.FileInput(attrs={'id': 'lefteye'}),
            'righteye': forms.FileInput(attrs={'id': 'righteye'}),
            'taken_at': forms.DateInput(attrs={'type':'date'}),
        }