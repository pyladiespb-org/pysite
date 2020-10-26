# Generated by Django 2.2.16 on 2020-10-07 00:37

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Eventos',
            fields=[
                ('id_evento', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('data_inicial', models.DateField()),
                ('data_final', models.DateField(blank=True, null=True)),
                ('titulo', models.CharField(max_length=200)),
                ('local', models.CharField(max_length=200)),
            ],
        ),
    ]