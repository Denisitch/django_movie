from django.shortcuts import render
from django.views.generic.base import View

from movies.models import Movie


class MoviesView(View):
    """Список фильмов"""
    @staticmethod
    def get(request):
        movies = Movie.objects.all()
        return render(request, 'movies/movies.html', {'movie_list': movies})