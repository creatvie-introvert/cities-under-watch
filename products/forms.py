from django import forms

from .models import Collection, Product, ProductImage, ProductDownload


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = (
            'collection',
            'title',
            'slug',
            'sku',
            'short_description',
            'description',
            'context_text',
            'price',
            'is_active',
            'is_featured',
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        available_collections = Collection.objects.filter(
            release_status=Collection.ReleaseStatus.AVAILABLE,
            city__is_active=True,
        ).select_related('city').order_by('name')

        self.fields['collection'].queryset = available_collections
        self.fields['collection'].empty_label = 'Select a collection'

        self.fields['collection'].widget.attrs.update({
            'class': 'product-admin-form__select',
        })
        self.fields['title'].widget.attrs.update({
            'class': 'product-admin-form__input',
            'placeholder': 'Product title',
        })
        self.fields['slug'].widget.attrs.update({
            'class': 'product-admin-form__input',
            'placeholder': 'product-slug',
        })
        self.fields['sku'].widget.attrs.update({
            'class': 'product-admin-form__input',
            'placeholder': 'SKU',
        })
        self.fields['short_description'].widget.attrs.update({
            'class': 'product-admin-form__input',
            'placeholder': 'Short description',
        })
        self.fields['description'].widget.attrs.update({
            'class': 'product-admin-form__textarea',
            'placeholder': 'Full product description',
        })
        self.fields['context_text'].widget.attrs.update({
            'class': 'product-admin-form__textarea',
            'placeholder': 'Narrative or contextual description',
        })
        self.fields['price'].widget.attrs.update({
            'class': 'product-admin-form__input',
            'placeholder': '0.00',
        })

        self.fields['is_active'].widget.attrs.update({
            'class': 'product-admin-form__checkbox',
        })
        self.fields['is_featured'].widget.attrs.update({
            'class': 'product-admin-form__checkbox',
        })


class ProductImageForm(forms.ModelForm):
    class Meta:
        model = ProductImage
        fields = (
            'image',
            'alt_text',
            'is_primary',
            'sort_order',
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['image'].widget.attrs.update({
            'class': 'product-admin-form__input',
        })
        self.fields['alt_text'].widget.attrs.update({
            'class': 'product-admin-form__input',
            'placeholder': "Image alt text",
        })
        self.fields['is_primary'].widget.attrs.update({
            'class': 'product-admin-form__checkbox',
        })
        self.fields['sort_order'].widget.attrs.update({
            'class': 'product-admin-form__input',
            'placeholder': '0',
        })

    def clean_image(self):
        image = self.cleaned_data.get('image')

        if self.instance and self.instance.pk and not image:
            return self.instance.image

        return image


class ProductDownloadForm(forms.ModelForm):
    class Meta:
        model = ProductDownload
        fields = (
            'title',
            'file',
            'sort_order',
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['title'].widget.attrs.update({
            'class': 'product-admin-form__input',
            'placeholder': 'Download title',
        })
        self.fields['file'].widget.attrs.update({
            'class': 'product-admin-form__input',
        })
        self.fields['sort_order'].widget.attrs.update({
            'class': 'product-admin-form__input',
            'placeholder': '0',
        })

    def clean_file(self):
        file = self.cleaned_data.get('file')

        if self.instance and self.instance.pk and not file:
            return self.instance.file

        return file
