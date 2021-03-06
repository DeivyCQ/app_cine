# Generated by Django 3.1.3 on 2020-11-16 04:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Billboard_Schedule',
            fields=[
                ('billboard_schedule_id', models.AutoField(primary_key=True, serialize=False)),
                ('scheduled_date', models.DateField()),
                ('scheduled_start_time', models.TimeField()),
                ('scheduled_end_time', models.TimeField()),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Programación Diaria de Cartelera',
                'verbose_name_plural': 'Programación Diaria de Cartelera',
            },
        ),
        migrations.CreateModel(
            name='Cinema',
            fields=[
                ('cinema_id', models.AutoField(primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=50)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Cine',
                'verbose_name_plural': 'Cines',
            },
        ),
        migrations.CreateModel(
            name='Customers',
            fields=[
                ('customer_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=80)),
                ('last_name', models.CharField(max_length=80)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Cliente',
                'verbose_name_plural': 'Clientes',
            },
        ),
        migrations.CreateModel(
            name='Film',
            fields=[
                ('film_id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=50)),
                ('synopsis', models.TextField(blank=True, null=True)),
                ('movie_trailer', models.CharField(blank=True, max_length=255, null=True)),
                ('country', django_countries.fields.CountryField(max_length=2)),
                ('year', models.PositiveIntegerField()),
                ('classification', models.CharField(blank=True, max_length=50, null=True)),
                ('duration', models.PositiveIntegerField()),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Película',
                'verbose_name_plural': 'Películas',
            },
        ),
        migrations.CreateModel(
            name='Film_Genre',
            fields=[
                ('film_genre_id', models.AutoField(primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=20)),
            ],
            options={
                'verbose_name': 'Género de Película',
                'verbose_name_plural': 'Géneros de Película',
            },
        ),
        migrations.CreateModel(
            name='Movie_Billboard',
            fields=[
                ('movie_billboard_id', models.AutoField(primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=50)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Cartelera',
                'verbose_name_plural': 'Carteleras',
            },
        ),
        migrations.CreateModel(
            name='Movie_Billboard_Cinema',
            fields=[
                ('movie_billboard_cinema_id', models.AutoField(primary_key=True, serialize=False)),
                ('scheduled_start_date', models.DateField()),
                ('scheduled_end_date', models.DateField()),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('cinema_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cinemex.cinema')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('movie_billboard_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cinemex.movie_billboard')),
            ],
            options={
                'verbose_name': 'Cartelera de Cine',
                'verbose_name_plural': 'Carteleras de Cine',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('order_id', models.AutoField(primary_key=True, serialize=False)),
                ('order_date', models.DateField()),
                ('room_id', models.IntegerField(blank=True, null=True)),
                ('total', models.DecimalField(decimal_places=2, max_digits=8)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('billboard_schedule_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cinemex.billboard_schedule')),
                ('customer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cinemex.customers')),
            ],
            options={
                'verbose_name': 'Pedido de venta',
                'verbose_name_plural': 'Pedidos de venta',
            },
        ),
        migrations.CreateModel(
            name='Room_Type',
            fields=[
                ('room_type', models.AutoField(primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=20)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Tipo de Sala',
                'verbose_name_plural': 'Tipos de Sala',
            },
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('room_id', models.AutoField(primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=20)),
                ('stock', models.DecimalField(decimal_places=3, max_digits=6)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('cinema_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cinemex.cinema')),
                ('room_type_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cinemex.room_type')),
            ],
            options={
                'verbose_name': 'Sala',
                'verbose_name_plural': 'Salas',
            },
        ),
        migrations.CreateModel(
            name='Order_Detail',
            fields=[
                ('position', models.IntegerField(primary_key=True, serialize=False)),
                ('armchair_id', models.IntegerField(blank=True, null=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('amount', models.IntegerField()),
                ('category_person_id', models.IntegerField()),
                ('user_category_id', models.IntegerField()),
                ('order_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='cinemex.order')),
            ],
            options={
                'verbose_name': 'Detalle de Pedido de Venta',
                'verbose_name_plural': 'Detalles de Pedido de Venta',
            },
        ),
        migrations.CreateModel(
            name='Movie_Billboard_Cinema_Film',
            fields=[
                ('movie_billboard_cinema_film_id', models.AutoField(primary_key=True, serialize=False)),
                ('premiere', models.BooleanField(default=False)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('film_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cinemex.film')),
                ('movie_billboard_cinema_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cinemex.movie_billboard_cinema')),
            ],
            options={
                'verbose_name': 'Cartelera de Película',
                'verbose_name_plural': 'Carteleras de Película',
            },
        ),
        migrations.AddField(
            model_name='film',
            name='film_genre_id',
            field=models.ManyToManyField(to='cinemex.Film_Genre'),
        ),
        migrations.AddField(
            model_name='billboard_schedule',
            name='movie_billboard_cinema_film_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cinemex.movie_billboard_cinema_film'),
        ),
        migrations.AddField(
            model_name='billboard_schedule',
            name='room_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cinemex.room'),
        ),
    ]
