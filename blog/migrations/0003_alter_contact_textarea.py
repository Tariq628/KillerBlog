# Generated by Django 4.0.2 on 2022-02-11 19:23

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20201227_1148'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='textarea',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
