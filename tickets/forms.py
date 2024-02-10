from django import forms
from .models import ticket

class InputForm(forms.ModelForm):
    class Meta:
        model = ticket
        fields = ['numbers']

    