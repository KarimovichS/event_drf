# Generated by Django 5.0.4 on 2024-04-15 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0007_remove_user_gmail_verif'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='gmail_code',
            field=models.CharField(blank=True, max_length=6, null=True),
        ),
    ]
