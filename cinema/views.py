from django.shortcuts import render, get_object_or_404
import logging
from cinema.models import Movie, Session

logger = logging.getLogger(__name__)


def home(request):
    movies = Movie.objects.all().order_by('-retease_date')


    context = {
        'movies': movies,
    }
    logger.info('INFO0000000000')
    return render(request, 'cinema/home.html', context)


def movie_detail(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    sessions = Session.objects.filter(movie=movie).order_by('start_time')



    context = {
        'movie':movie,
        'session': sessions
    }
    return render(request,'cinema/movie_detail.html', context)

