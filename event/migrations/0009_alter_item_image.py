# Generated by Django 5.0.4 on 2024-04-11 11:34

import event.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0008_alter_event_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='image',
            field=models.FileField(upload_to='item/', validators=[event.validators.validate_svg]),
        ),
    ]
