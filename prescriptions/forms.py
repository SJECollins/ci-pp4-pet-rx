from django import forms
from .models import Prescription


class PrescrForm(forms.ModelForm):
    """
    Model form for prescriptions
    """
    class Meta:
        model = Prescription
        fields = ['drug', 'frequency', 'length', ]
