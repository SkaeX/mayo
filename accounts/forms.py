from django import forms
from django.contrib.auth.models import Group


class MayoSignupForm(forms.Form):
    roles = (
        ('Mentee', 'I am here to be mentored'),
        ('Mentor', 'I am here to mentor'),
    )
    role = forms.ChoiceField(choices=roles, label='Role', initial=roles[0][0])

    def signup(self, request, user):
        grp = Group.objects.get(name=self.cleaned_data['role'])
        user.groups.add(grp)
