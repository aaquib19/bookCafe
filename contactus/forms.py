from django import forms


class ContactForm(forms.Form):

    from_email = forms.EmailField(
        label='',
        widget=forms.EmailInput(
            attrs={
                'placeholder': 'Email (example@gmail.com)',
                'class': 'form-control',
                'id': 'staticEmail'
            }
        )
    )

    subject = forms.CharField(
        label='',
        widget=forms.TextInput(
            attrs={
                'placeholder': 'SUBJECT',
                'width': '500px',
                'class': 'form-control',
                'oninvalid': 'this.setCustomValidity("Please fill this field")'
            }
        )
    )

    message = forms.CharField(
        label='Feel free to add any other comments or suggestions:',
        widget=forms.Textarea(
            attrs={
                'placeholder': 'Type your suggestions here...',
                'width': '500px',
                'class': 'form-control',
                'oninvalid': 'this.setCustomValidity("Please write your feedback in this field")'
            }
        )
    )
