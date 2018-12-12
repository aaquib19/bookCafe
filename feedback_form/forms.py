from django import forms

from .models import Feedback


class FeedbackForm(forms.ModelForm):
    customer_name = forms.CharField(
        label='',
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Fullname',
                'class': 'form-control',
                'rows': '3',
                'id': 'staticEmail'
            }
        )
    )

    email = forms.EmailField(
        label='',
        widget=forms.EmailInput(
            attrs={
                'placeholder': 'Email (example@gmail.com)',
                'class': 'form-control',
                'id': 'staticEmail'
            }
        )
    )

    comments = forms.CharField(
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

    book_name = forms.CharField(
        label='Feel free to add any other comments or suggestions:',
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Book name',
                'width': '500px',
                'class': 'form-control',
                'oninvalid': 'this.setCustomValidity("Please fill this field")'
            }
        )
    )

    class Meta:
        model = Feedback
        fields = ['customer_name', 'email', 'comments', 'book_name']
