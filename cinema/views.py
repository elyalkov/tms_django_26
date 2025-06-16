from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
import logging

from cinema.forms import BookingForm
from cinema.models import Movie, Session, Booking

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

    sessions_by_date = {}
    for sessin in sessions:
        date = sessin.start_time.date()
        if date not in sessions_by_date:
            sessions_by_date[date] = []
        sessions_by_date[date].append(sessin)

    print(sessions_by_date)

    context = {'movie':movie,'session': sessions}
    return render(request,'cinema/movie_detail.html', context)

@login_required
def book_ticket(request, session_id):
    session = get_object_or_404(Session, pk=session_id)

    if request.method == 'POST':
        form = BookingForm(request.POST, session=session)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.session = session
            booking.status = 'confirmed'
            booking.save()

            logger.info(f'New booking created: {booking}')
            return redirect('profile')
        else:
            form = BookingForm(session=session)

        #Получаем занятые места для этого сеанса
        taken_seats = Booking.objects.filter(
            session=session,
            status__in=['confirmed', 'pending']
        ).values_list('seat', flat=True)

        context = {
            'session': session,
            'form': form,
            'taken_seats': taken_seats,
        }
        return render(request, 'cinema/book_ticket.html', context)