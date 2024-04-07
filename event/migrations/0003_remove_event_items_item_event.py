# Generated by Django 5.0.4 on 2024-04-07 09:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0002_userevent_items'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='items',
        ),
        migrations.AddField(
            model_name='item',
            name='event',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='event_items', to='event.event'),
            preserve_default=False,
        ),
    ]
