from django import forms

from .models import UserProfile


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ('user',)

    def __init__(self, *args, **kwargs):
        """Add placeholder, remove labels, and apply shared styling classes."""
        super().__init__(*args, **kwargs)

        placeholders = {
            'full_name': 'Full name',
            'phone_number': 'Phone number',
            'country_code': 'Country code',
            'postcode': 'Postcode',
            'town_or_city': 'Town or city',
            'street_address1': 'Street address 1',
            'street_address2': 'Street address 2',
            'county': 'County',
        }

        self.fields['full_name'].widget.attrs['autofocus'] = True

        for field_name, field in self.fields.items():
            placeholder = placeholders[field_name]
            field.widget.attrs['placeholder'] = placeholder
            field.widget.attrs['class'] = 'checkout-form__input'
            field.label = False
