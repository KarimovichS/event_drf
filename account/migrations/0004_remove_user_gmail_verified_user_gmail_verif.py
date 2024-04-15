# Generated by Django 5.0.4 on 2024-04-15 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_alter_user_gmail_verified'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='gmail_verified',
        ),
        migrations.AddField(
            model_name='user',
            name='gmail_verif',
            field=models.CharField(blank=True, default='DEFAULT_VALUE', max_length=6, null=True),
        ),
    ]