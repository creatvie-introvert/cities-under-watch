from django import forms

from .models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = (
            'full_name',
            'email',
            'phone_number',
            'country_code',
            'postcode',
            'town_or_city',
            'street_address1',
            'street_address2',
            'county',
        )

    def __init__(self, *args, **kwargs):
        """
        Add placeholders, remove labels, and apply shared styling classes.
        """
        super().__init__(*args, **kwargs)

        placeholders = {
            'full_name': 'Full name',
            'email': 'Email address',
            'phone_number': 'Phone number',
            'country_code': 'Country code',
            'postcode': 'Postcode',
            'town_or_city': 'Town or City',
            'street_address1': 'Street address 1',
            'street_address2': 'Street address 2',
            'county': 'County',
        }

        self.fields['full_name'].widget.attrs['autofocus'] = True

        for field_name, field in self.fields.items():
            placeholder = placeholders[field_name]

            if field.required:
                placeholder = f'{placeholder} *'

            field.widget.attrs['placeholder'] = placeholder
            field.widget.attrs['class'] = 'checkout-form__input'
            field.label = False
