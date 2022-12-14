from django.conf import settings
from django.db import models


class Ticket(models.Model):
    title = models.CharField(max_length=128)
    lien_cadeau = models.TextField(max_length=128, blank=True)
    user = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    image_url = models.CharField(max_length=128, blank=True)
    time_created = models.DateTimeField(auto_now_add=True)
    reserve = models.BooleanField(default=False, verbose_name="reserved")
    def __str__(self):
        return self.title