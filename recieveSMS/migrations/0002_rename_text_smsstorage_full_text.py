# Generated by Django 4.0.5 on 2022-06-20 13:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recieveSMS', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='smsstorage',
            old_name='text',
            new_name='full_text',
        ),
    ]