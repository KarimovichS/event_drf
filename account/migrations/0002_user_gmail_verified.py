# Generated by Django 5.0.4 on 2024-04-15 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='gmail_verified',
            field=models.CharField(blank=True, default=None, max_length=6),
        ),
    ]
