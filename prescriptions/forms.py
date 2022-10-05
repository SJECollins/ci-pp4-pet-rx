from django import forms
from dynamic_forms import DynamicField, DynamicFormMixin
from .models import Category, Drug, Prescription


FREQUENCY = (('No Repeat', 'No Repeat'), ('SID', 'SID'),
             ('BID', 'BID'), ('TID', 'TID'))


class PrescrForm(DynamicFormMixin, forms.ModelForm):
    """
    Model form for prescriptions.
    From BugBytes, see link in credits of readme.
    """
    def drug_choices(self):
        """
        Method to filter drugs by category.
        """
        category = self['category'].value()
        return Drug.objects.filter(category=category)

    def initial_drug(self):
        """
        Method to display first drug in category
        """
        category = self['category'].value()
        return Drug.objects.filter(category=category).first()

    category = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        initial=Category.objects.first()
    )

    drug = DynamicField(
        forms.ModelChoiceField,
        queryset=drug_choices,
        initial=initial_drug
    )

    frequency = forms.CharField(
        max_length=10,
        widget=forms.Select(choices=FREQUENCY),
        required=False
    )

    length = forms.IntegerField(
        initial=0,
        widget=forms.NumberInput(attrs={'min': 0,'max': 7, 'step_size': 1}),
        required=False
    )

    class Meta:
        model = Prescription
        fields = ['category', 'drug', 'frequency', 'length', ]
