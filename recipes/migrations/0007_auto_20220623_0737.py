# Generated by Django 3.2.13 on 2022-06-23 07:37

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0006_alter_recepte_directions'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='content',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='ingridients',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
