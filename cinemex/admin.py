from django.contrib import admin
from .models import Cinema, Movie_Billboard, Movie_Billboard_Cinema, Film, Film_Genre, Movie_Billboard_Cinema_Film, Room_Type, Room, Billboard_Schedule, Customers, Order, Order_Detail

# Register your models here.
admin.site.register(Cinema)
admin.site.register(Movie_Billboard)
admin.site.register(Movie_Billboard_Cinema)
admin.site.register(Film)
admin.site.register(Film_Genre)
admin.site.register(Movie_Billboard_Cinema_Film)
admin.site.register(Room_Type)
admin.site.register(Room)
admin.site.register(Billboard_Schedule)
admin.site.register(Customers)
admin.site.register(Order)
admin.site.register(Order_Detail)