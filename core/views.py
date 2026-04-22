from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import render, redirect

from .forms import NewsletterSubscriberForm, ContactForm
from .models import NewsletterSubscriber
from products.models import Product


def index(request):
    """Render the home page and handle newsletter signups."""
    if request.method == 'POST':
        newsletter_form = NewsletterSubscriberForm(request.POST)

        if newsletter_form.is_valid():
            email = newsletter_form.cleaned_data['email']

            if NewsletterSubscriber.objects.filter(email=email).exists():
                messages.info(
                    request,
                    'This email is already subscribed to updates.',
                )
            else:
                newsletter_form.save()
                messages.success(
                    request,
                    'Thanks for sunscrobing. You will be notified about new releases.'
                )

                return redirect('home')

            messages.error(
                request,
                'Please enter a valid email address.',
            )
            return redirect('home')

    featured_products = (
        Product.objects
        .filter(
            is_active=True,
            is_featured=True,
            collection__city__is_active=True,
        )
        .select_related('collection', 'collection__city')
        .prefetch_related('images')[:3]
    )

    newsletter_form = NewsletterSubscriberForm()

    context = {
        'featured_products': featured_products,
        'newsletter_form': newsletter_form,
    }

    return render(request, 'core/index.html', context)


def about(request):
    """Render the about page."""
    return render(request, 'core/about.html')


def contact(request):
    """Render and handle the contact page."""
    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']

            full_subject = f'Contact form: {subject}'
            full_message = (
                f'Name: {name}\n'
                f'Email: {email}\n\n'
                f'Message: \n{message}'
            )

            send_mail(
                subject=full_subject,
                message=full_message,
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[settings.CONTACT_EMAIL],
                fail_silently=False,
            )

            messages.success(
                request,
                'Your message has been sent successfully.',
            )
            return redirect('contact')

        messages.error(
            request,
            'There was a problem with your form. Please check your details.'
        )
    else:
        form = ContactForm()

    context = {
        'form': form,
    }
    return render(request, 'core/contact.html', context)


def faq(request):
    """Render the FAQ page."""
    return render(request, 'core/faq.html')


def privacy_policy(request):
    """Render the privacy policy page."""
    return render(request, 'core/privacy_policy.html')


def terms_and_conditions(request):
    """Render the terms and conditions page."""
    return render(request, 'core/terms_and_conditions.html')


def refund_policy(request):
    """Render the refund policy page."""
    return render(request, 'core/refund_policy.html')


def delivery_policy(request):
    """Render the delivery policy page."""
    return render(request, 'core/delivery_policy.html')
