# Generated by Django 4.0.6 on 2022-11-14 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0005_remove_ticket_image_ticket_image_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='lien_cadeau',
            field=models.TextField(blank=True, max_length=2048),
        ),
    ]
