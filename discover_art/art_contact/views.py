from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.views.generic import CreateView
from django.urls import reverse_lazy

from discover_art.art_contact.forms import ContactForm
from discover_art.art_contact.models import ArtContact


class ContactView(CreateView):
    template_name = 'contact.html'
    model = ArtContact
    form_class = ContactForm
    success_url = reverse_lazy('contact message')


def contact_message(request):
    return render(request, 'contact_us_message.html')