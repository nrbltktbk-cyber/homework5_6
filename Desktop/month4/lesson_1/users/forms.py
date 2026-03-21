from django import forms
from . import models
from django.contrib.auth.forms import UserCreationForm

GENDER = (
        ('MALE', 'MALE'),
        ('FEMALE', 'FEMALE')
    )


class CustomRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    phone_number = forms.CharField(max_length=15, initial='+996', required=True)
    gender = forms.ChoiceField(choices=GENDER, required=True)
    city = forms.CharField(max_length=100, required=True)

    class Meta:
        model = models.CustomUser
        fields = (
            "username",
            "password1",
            "password2",
            "first_name",
            "last_name",
            "email",
            "phone_number",
            "gender",
            "city"
        )
    
    def save(self, commit = True):
        user = super(CustomRegisterForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user