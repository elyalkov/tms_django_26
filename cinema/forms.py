from django import forms
from .models import Booking, Movie
from django.core.validators import MinValueValidator, MaxValueValidator



class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['seat']

    def __init__(self, *args, **kwargs):
        self.session = kwargs.pop('session')
        super().__init__(*args, **kwargs)

        #динамически создае выбор мест
        seats = []
        for row in range(1, 6): #5 рядов (А-Е)
            for seat_num in range(1, 11): #10 мест в ряду
                seat = f'{chr(64 + row)}{seat_num}'
                seats.append((seat, seat))

        self.fields['seat'] = forms.ChoiceField(
            choices=seats,
            label='Выберите место'
        )

    def clean_seat(self):
        seat = self.cleaned_data['seat']
        if Booking.objects.filter(
            session=self.session,
            seat=seat,
            status__in=['confirmed', 'pending']
        ).exists():
            raise forms.ValidationError('Это место уже занято')
        return seat



class MovieFilterForm(forms.Form):
    SORT_CHOICES = [
        ('-retease_date', 'По дате выхода (нвоые)'),
        ('retease_date', 'По дате выхода (старые)'),
        ('-rating', 'По рейтингу (высокий)'),
        ('rating', 'По рейтингу (низкий)'),
        ('title', 'По названию (А-Я)'),
        ('-title', 'По названию (Я-А)'),
    ]

    search = forms.CharField(
        required=False,
        label='Поиск',
        widget=forms.TextInput(attrs={'placeholder': 'Фильм, актер, режиссер'})
    )
    genre = forms.ModelChoiceField(
        queryset=Genre.objects.all(),
        required=False,
        label='Жанр',
        empty_label='Все жанры'
    )
    sort = forms.CharField(
        choices=SORT_CHOICES,
        required=False,
        label='Сортировка',
    )