# Generated by Django 3.2.12 on 2022-03-28 12:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movieapp', '0002_movie_img'),
    ]

    operations = [
        migrations.RenameField(
            model_name='movie',
            old_name='img',
            new_name='image',
        ),
    ]
