from django import forms
from .models import Field, Prequest, Program


class FieldForm(forms.models.ModelForm):
    class Meta:
        model = Field
        fields = ('title', 'description')
        widgets = {
            'title': forms.fields.TextInput(attrs={
                'placeholder': 'Enter a title',
            }),
        }


class IndividualPrequestForm(forms.models.ModelForm):
    class Meta:
        model = Prequest
        fields = ['field']
        help_texts = {
            'field': 'Please if you cannot find your desire field in the list, contact ^^ MAYO team for assistance'
        }


class PrequestForm(forms.models.ModelForm):
    class Meta:
        model = Prequest
        fields = ('field', 'pending', 'requester')


class ProgramForm(forms.models.ModelForm):
    class Meta:
        model = Program
        fields = ('title', 'description', 'in_progress', 'prequest', 'mentors', 'mentees')
