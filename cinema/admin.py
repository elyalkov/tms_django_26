from django.contrib import admin
from cinema.models import Genre, Director, Actors, Movie, CinemaHall, Session, Booking


class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'retease_date', 'rating')
    list_filter = ('genres', 'retease_date')
    search_fields = ('title', 'directors__first_name', 'directors__last_name') #не забывать про двойное __
    filter_horizontal = ('genres', 'actors')


class SessionAdmin(admin.ModelAdmin):
    list_display = ('movie', 'start_time', 'hall', 'price')
    list_filter = ('start_time', 'hall')
    search_fields = ('movie__title', )#не забывать про запятую


class BookingAdmin(admin.ModelAdmin):
    list_display = ('user', 'session', 'seat', 'status', 'booked_at')
    list_filter = ('status', 'booked_at')
    search_fields = ('user__username', 'session__movie__title')


admin.site.register(Genre)
admin.site.register(Director)
admin.site.register(Actors)
admin.site.register(Movie, MovieAdmin)
admin.site.register(CinemaHall)
admin.site.register(Session, SessionAdmin)
admin.site.register(Booking, BookingAdmin)