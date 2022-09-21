from django import forms
from .models import Record
from django.core.exceptions import NON_FIELD_ERRORS


class RecordForm(forms.ModelForm):
    class Meta:
        model = Record
        fields = ['name', 'surname', 'date_of_birth', 'species', 'breed', 'sex', 'weight']
        error_messages = {
            NON_FIELD_ERRORS: {
                'unique_together': "A record already exists with the same %(field_labels)s.",
            }
        }
