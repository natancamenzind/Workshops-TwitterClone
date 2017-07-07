from django import forms
from django.contrib.auth import authenticate


class UserLoginForm(forms.Form):
    class UserLoginForm(forms.Form):
        username = forms.CharField(max_length=150)
        password = forms.CharField(widget=forms.PasswordInput)

        def clean(self):
            cleaned_data = super(UserLoginForm,self).clean()
            user = authenticate(
                username=cleaned_data['username'],
                password=cleaned_data['password'],
            )

            if user is None:
                raise forms.ValidationError(
                    'Coś... coś się zepsuło ...'
                )
            cleaned_data['user'] = user
            return cleaned_data

