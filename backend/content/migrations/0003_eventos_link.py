# Generated by Django 2.2.16 on 2020-10-07 00:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0002_eventos'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventos',
            name='link',
            field=models.URLField(default=' '),
        ),
    ]
