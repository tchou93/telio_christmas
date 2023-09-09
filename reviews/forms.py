from django import forms
from reviews.models import Ticket

class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['title', 'lien_cadeau','image']
        labels = {"title": "Titre",
                  "lien_cadeau" : "Adresse du cadeau",
                  "image": "Image",
                  }

class UpdateTicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['title', 'lien_cadeau','image', 'reserve']
        labels = {"title": "Titre",
                  "lien_cadeau" : "Adresse du cadeau",
                  "image": "Image",
                  "reserve": "Réservation",
                  }