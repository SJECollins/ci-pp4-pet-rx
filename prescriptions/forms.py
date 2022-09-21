from django import forms
from .models import Prescription


class PrescrForm(forms.ModelForm):
    class Meta:
        model = Prescription
        fields = ['animal', 'animal_weight', 'drug', 'drug_dose', 'route']