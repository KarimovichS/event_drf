# Generated by Django 5.0.4 on 2024-04-15 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_user_gmail_verified'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='gmail_verified',
            field=models.CharField(blank=True, default=True, max_length=6, null=True),
        ),
    ]