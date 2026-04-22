from django import forms

from .models import NewsletterSubscriber


class NewsletterSubscriberForm(forms.ModelForm):
    class Meta:
        model = NewsletterSubscriber
        fields = ('email',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].widget.attrs.update({
            'id': 'newsletter-email',
            'class': 'newsletter-form__input',
            'placeholder': 'Enter your email',
        })
        self.fields['email'].label = ''


class ContactForm(forms.Form):
    name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'contact-form__input',
            'placeholder': 'Your name',
        }),
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'class': 'contact-form__input',
            'placeholder': 'Your email address',
        }),
    )
    subject = forms.CharField(
        max_length=150,
        widget=forms.TextInput(attrs={
            'class': 'contact-form__input',
            'placeholder': 'What is your message about?',
        }),
    )
    message = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'contact-form__textarea',
            'placeholder': 'Tell us how we can help',
        }),
    )
