# Generated by Django 5.0.4 on 2024-04-15 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_alter_user_gmail_verif'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='gmail_verif',
            field=models.CharField(blank=True, default='0', max_length=6, null=True),
        ),
    ]
