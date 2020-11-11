# Generated by Django 3.1.3 on 2020-11-11 05:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cinema',
            fields=[
                ('cinema_id', models.AutoField(primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Cine',
                'verbose_name_plural': 'Cines',
            },
        ),
    ]