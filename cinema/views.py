from django.shortcuts import render
import logging
from cinema.models import Movie

logger = logging.getLogger(__name__)


def home(request):
    movies = Movie.objects.all().order_by('-retease_date')


    context = {
        'movies': movies,
    }
    logger.info('INFO0000000000')
    return render(request, 'cinema/home.html', context)


