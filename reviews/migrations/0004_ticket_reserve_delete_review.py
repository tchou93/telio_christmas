# Generated by Django 4.0.6 on 2022-11-14 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0003_alter_ticket_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='reserve',
            field=models.BooleanField(default=False, verbose_name='reserved'),
        ),
        migrations.DeleteModel(
            name='Review',
        ),
    ]
