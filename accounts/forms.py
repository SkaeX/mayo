from django import forms
from django.contrib.auth.models import Group
from .models import User


class MayoSignupForm(forms.Form):
    roles = (
        ('Mentee', 'I am here to be mentored'),
        ('Mentor', 'I am here to mentor'),
    )
    role = forms.ChoiceField(choices=roles, label='Role', initial=roles[0][0])
    first_name = forms.CharField(max_length=50, label='First Name', widget=forms.TextInput(attrs={'autofocus': 'autofocus'}))
    last_name = forms.CharField(max_length=50, label='Last Name')

    def signup(self, request, user):
        grp = Group.objects.get(name=self.cleaned_data['role'])
        user.groups.add(grp)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()


class UserEditForm(forms.models.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'groups', 'is_active')
        widgets = {
            'first_name': forms.fields.TextInput(attrs={
                'placeholder': 'Enter a first name',
                'class': 'form-control',
            }),
            'last_name': forms.fields.TextInput(attrs={
                'placeholder': 'Enter a last name',
                'class': 'form-control',
            }),
            'email': forms.fields.EmailInput(attrs={
                'placeholder': 'Enter an email',
                'class': 'form-control',
            }),
            'groups': forms.fields.SelectMultiple(attrs={
                'class': 'form-control',
            }),
        }