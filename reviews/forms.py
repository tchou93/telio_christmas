from django import forms
from reviews.models import Ticket

class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['title', 'lien_cadeau','image_url']
        labels = {"title": "Titre",
                  "lien_cadeau" : "Adresse du cadeau",
                  "image_url": "Adresse de l'image",
                  }

class UpdateTicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['title', 'lien_cadeau','image_url', 'reserve']
        labels = {"title": "Titre",
                  "lien_cadeau" : "Adresse du cadeau",
                  "image_url": "Adresse de l'image",
                  "reserve": "Réservation",
                  }