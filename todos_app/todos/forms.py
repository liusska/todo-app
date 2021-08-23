from django import forms
from django.core.validators import ValidationError


def validate_dot(value_to_validate):
    if '.' in value_to_validate:
        raise forms.ValidationError('\'.\' is present in value!')


class CreateTodoFrom(forms.Form):
    title = forms.CharField(
        max_length=30,
        validators=[
            validate_dot
        ]
    )
    description = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'class': 'my-text-area',
                'rows': 3,
                'placeholder': 'Enter todo description',
            }
        )
    )

    bots_catcher = forms.CharField(
        widget=forms.HiddenInput(),
        required=False,
    )

    def clean_bot_catcher(self):
        value = self.cleaned_data['bots_catcher']

        if value:
            raise ValidationError('You are a bot')
