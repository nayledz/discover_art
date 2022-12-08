from django import forms

from discover_art.art_contact.models import ArtContact


class ContactForm(forms.ModelForm):
    class Meta:
        model = ArtContact
        fields = '__all__'
        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Last Name'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email'}),
            'message': forms.Textarea(attrs={'placeholder': 'What do you think about "DiscoverArt"?', 'rows': 6}),
        }