from django import forms
from .models import Record
from django.core.exceptions import NON_FIELD_ERRORS


class DateInput(forms.DateInput):
    input_type = 'date'


class RecordForm(forms.ModelForm):
    """
    Modelform for Record.
    """
    class Meta:
        """
        Add non_field_error for unique_together constraint.
        """
        model = Record
        fields = ['name', 'surname', 'date_of_birth', 'species', 'breed', 'sex', 'weight']
        widgets = {
            'date_of_birth': DateInput(),
        }
        error_messages = {
            NON_FIELD_ERRORS: {
                'unique_together': "A record already exists with the same %(field_labels)s.",
            }
        }


class WeightForm(forms.ModelForm):
    """
    ModelForm for weight so user can update.
    """
    class Meta:
        """
        Only want weight field.
        """
        model = Record
        fields = ['weight', ]


class NoteForm(forms.ModelForm):
    """
    ModelForm for note on animal's record.
    """
    class Meta:
        """
        Add widget for textarea.
        """
        model = Record
        fields = ['note', ]
        widgets = {
            'note': forms.Textarea(attrs={'cols': 30, 'rows': 10}),
        }
