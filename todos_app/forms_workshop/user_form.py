from django import forms

'''
Name: CharField
Age: IntegerField with NumberInput widget
Email: EmailField with EmailInput widget
Password: CharField with PasswordInput widget
Text: CharField with Textarea widget

'''


class UserForm(forms.Form):
    name = forms.CharField()

    age = forms.IntegerField(
        widget=forms.NumberInput,
    )
    email = forms.EmailField()

    password = forms.CharField(
        widget=forms.PasswordInput(),
    )

    text = forms.CharField(
        widget=forms.Textarea(),
    )

    def clean_password(self):
        pure_password = self.cleaned_data['password']
        return f'!{pure_password}!'
