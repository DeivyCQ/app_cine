from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django_countries.fields import CountryField

# Create your models here.

# Cinema Model.
class Cinema(models.Model):
    cinema_id = models.AutoField(primary_key=True)
    description = models.CharField(max_length=50, blank=False, null=False)
    created_date = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.description

    class Meta:
        verbose_name = 'Cine'
        verbose_name_plural = 'Cines'

class Movie_Billboard(models.Model):
    movie_billboard_id = models.AutoField(primary_key=True)
    description = models.CharField(max_length=50, blank=False, null=False)
    created_date = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.description

    class Meta:
        verbose_name = 'Cartelera'
        verbose_name_plural = 'Carteleras'

class Movie_Billboard_Cinema(models.Model):
    movie_billboard_cinema_id = models.AutoField(primary_key=True)
    cinema_id = models.ForeignKey(Cinema, on_delete=models.CASCADE)
    movie_billboard_id = models.ForeignKey(Movie_Billboard, on_delete=models.CASCADE)
    scheduled_start_date = models.DateField(auto_now=False, auto_now_add=False)
    scheduled_end_date = models.DateField(auto_now=False, auto_now_add=False)
    created_date = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        # return (self.cinema_id, self.movie_billboard_id, str(self.scheduled_start_date), str(self.scheduled_end_date))
        return self.cinema_id

    class Meta:
        verbose_name = 'Cartelera de Cine'
        verbose_name_plural = 'Carteleras de Cine'

class Film_Genre(models.Model):
    film_genre_id = models.AutoField(primary_key=True)
    description = models.CharField(max_length=20, blank=False, null=False)

    def __str__(self):
        return self.description

    class Meta:
        verbose_name = 'Género de Película'
        verbose_name_plural = 'Géneros de Película'

class Film(models.Model):
    film_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50, blank=False, null=False)
    synopsis = models.TextField(blank=True, null=True)
    movie_trailer = models.CharField(max_length=255, blank=True, null=True)
    country = CountryField()
    year = models.PositiveIntegerField()
    classification = models.CharField(max_length=50, blank=True, null=True)
    duration = models.PositiveIntegerField()
    created_date = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    film_genre_id = models.ManyToManyField(Film_Genre)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Película'
        verbose_name_plural ='Películas'

class Movie_Billboard_Cinema_Film(models.Model):
    movie_billboard_cinema_film_id = models.AutoField(primary_key=True)
    movie_billboard_cinema_id = models.ForeignKey(Movie_Billboard_Cinema, on_delete=models.CASCADE)
    film_id = models.ForeignKey(Film, on_delete=models.CASCADE)
    premiere = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.movie_billboard_cinema_id

    class Meta:
        verbose_name = 'Cartelera de Película'
        verbose_name_plural = 'Carteleras de Película'

class Room_Type(models.Model):
    room_type = models.AutoField(primary_key=True)
    description = models.CharField(max_length=20, blank=False, null=False)
    created_date = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.description
    
    class Meta:
        verbose_name = 'Tipo de Sala'
        verbose_name_plural = 'Tipos de Sala'

class Room(models.Model):
    room_id = models.AutoField(primary_key=True)
    description = models.CharField(max_length=20, blank=False, null=False)
    stock = models.DecimalField(max_digits=6, decimal_places=3)
    room_type_id =models.ForeignKey(Room_Type, on_delete=models.CASCADE)
    cinema_id = models.ForeignKey(Cinema, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return [self.cinema_id, self.room_type_id, self.description]

    class Meta:
        verbose_name = 'Sala'
        verbose_name_plural = 'Salas'

class Billboard_Schedule(models.Model):
    billboard_schedule_id = models.AutoField(primary_key=True)
    room_id = models.ForeignKey(Room, on_delete=models.CASCADE)
    movie_billboard_cinema_film_id = models.ForeignKey(Movie_Billboard_Cinema_Film, on_delete=models.CASCADE)
    scheduled_date = models.DateField(blank=False, null=False)
    scheduled_start_time = models.TimeField(blank=False, null=False)
    scheduled_end_time = models.TimeField(blank=False, null=False)
    created_date = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.scheduled_date)

    class Meta:
        verbose_name = 'Programación Diaria de Cartelera'
        verbose_name_plural = 'Programación Diaria de Cartelera'

class Customers(models.Model):
    customer_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=80, blank=False, null=False)
    last_name = models.CharField(max_length=80, blank=False, null=False)
    created_date = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'

class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    customer_id = models.ForeignKey(Customers, on_delete=models.CASCADE)
    billboard_schedule_id = models.ForeignKey(Billboard_Schedule, on_delete=models.CASCADE)
    order_date = models.DateField(blank=False, null=False)
    room_id = models.IntegerField(blank=True, null=True)
    total = models.DecimalField(max_digits=8, decimal_places=2, blank=False, null=False)
    created_date = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.customer_id)
    
    class Meta:
        verbose_name = 'Pedido de venta'
        verbose_name_plural = 'Pedidos de venta'

class Order_Detail(models.Model):
    order_id = models.OneToOneField(Order, on_delete=models.CASCADE)
    position = models.IntegerField(primary_key=True)
    armchair_id = models.IntegerField(blank=True, null=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    amount = models.IntegerField(blank=False, null=False)
    category_person_id = models.IntegerField(blank=False, null=False)
    user_category_id = models.IntegerField(blank=False, null=False)

    def __str__(self):
        return self.position

    class Meta:
        verbose_name = 'Detalle de Pedido de Venta'
        verbose_name_plural = 'Detalles de Pedido de Venta'