# Generated by Django 5.2.3 on 2025-06-28 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donations', '0002_contact'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='checkbox',
        ),
        migrations.AddField(
            model_name='contact',
            name='consent',
            field=models.BooleanField(default=False, help_text='I agree to the privacy policy'),
        ),
    ]
