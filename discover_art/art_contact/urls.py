from django.urls import path

from discover_art.art_contact.views import ContactView, contact_message

urlpatterns = (
    path('contact/', ContactView.as_view(), name='contact us'),
    path('contact/contact-message', contact_message, name='contact message'),

)
