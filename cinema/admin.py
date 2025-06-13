from django.contrib import admin
from cinema.models import Genre, Director, Actors, Movie, CinemaHall, Session, Booking


admin.site.register(Genre)
admin.site.register(Director)
admin.site.register(Actors)
admin.site.register(Movie)
admin.site.register(CinemaHall)
admin.site.register(Session)
admin.site.register(Booking)