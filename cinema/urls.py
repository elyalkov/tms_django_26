from django.urls import path
from cinema import views


urlpatterns = [
    path('', views.home, name = 'home'),
    path('movie/<int:pk>/', views.movie_detail, name = 'movie_detail'),
]