from django import forms
from .models import Field, Request, Program


class FieldForm(forms.models.ModelForm):
    class Meta:
        model = Field
        fields = ('title', 'description')
        widgets = {
            'title': forms.fields.TextInput(attrs={
                'placeholder': 'Enter a title',
                'class': 'form-control',
            }),
        }


class RequestForm(forms.models.ModelForm):
    class Meta:
        model = Request
        fields = ('field', 'pending', 'mentee')


class ProgramForm(forms.models.ModelForm):
    class Meta:
        model = Program
        fields = ('title', 'description', 'in_progress', 'request', 'mentors', 'mentees')
