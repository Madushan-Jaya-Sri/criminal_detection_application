from django import forms
from .models import Suspect

class SuspectForm(forms.ModelForm):
    class Meta:
        model = Suspect
        fields = ['name', 'age', 'crime_incidents', 'arrest_reason', 'photo']
