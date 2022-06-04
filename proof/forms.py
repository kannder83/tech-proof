from django import forms

from .models import Register


class RegisterForm(forms.ModelForm):

    class Meta:
        model = Register
        fields = ('first_name', 'last_name', 'email', 'address',
                  'type_of_housing', 'country', 'department', 'city', 'date_of_birth', 'comments')
