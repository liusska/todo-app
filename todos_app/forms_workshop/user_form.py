from django import forms
from django.core.validators import ValidationError, MinLengthValidator


'''
Must start with an uppercase letter and have a minimum length of 6.
You can use a built-in validator for the minimum length.
Validation Error message: "The name must start with an uppercase letter."

'''


def validate_name(value):
    if not value[0] == value[0].upper():
        raise ValidationError("The name must start with an uppercase letter.")


'''
Must be bigger than or equal to 0
You can use the built-in validator for the validation or create your own
Validation Error message: "The age cannot be less than zero."

'''


def validate_age(value):
    if value < 0:
        raise ValidationError("The age cannot be less than zero.")


'''
Contains @ and dot
You can use the built-in validator for the validation
Validation Error message: "Enter a valid email."
'''


def validate_email(value):
    if not '@' in value:
        raise ValidationError("Enter a valid email.")


'''
Must have a minimum length of 8 and can only contain letters and numbers.
You can use a built-in validator for the minimum length and a custom one for the requirements
Validation Error message: "Enter a valid password."

'''


def validate_password(value):
    if len(value) < 8:
        raise ValidationError("Enter a valid password.")
    if any([not x.isalnum() for x in value]):
        raise ValidationError("Enter a valid password.")


'''
Name: CharField
Age: IntegerField with NumberInput widget
Email: EmailField with EmailInput widget
Password: CharField with PasswordInput widget
Text: CharField with Textarea widget

'''


class UserForm(forms.Form):
    name = forms.CharField(
        validators=[
            MinLengthValidator(6),
            validate_name,
        ]
    )

    age = forms.IntegerField(
        widget=forms.NumberInput,
        validators=[
            validate_age,
        ]
    )
    email = forms.EmailField()

    password = forms.CharField(
        widget=forms.PasswordInput(),
        validators=[
            validate_password,
        ]
    )

    text = forms.CharField(
        widget=forms.Textarea(),
    )

    def clean_password(self):
        pure_password = self.cleaned_data['password']
        return f'!{pure_password}!'

