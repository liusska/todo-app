from django import forms


class CreateTodoFrom(forms.Form):
    text = forms.CharField(
        max_length=30,
    )
    description = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'class': 'my-text-area',
                'rows': 3
            }
        )
    )
