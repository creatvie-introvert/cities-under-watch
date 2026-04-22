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
