# Generated by Django 4.0.2 on 2022-03-22 12:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_contact_textarea'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='textarea',
            new_name='content',
        ),
    ]