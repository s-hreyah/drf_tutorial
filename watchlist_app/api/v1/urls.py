from django.urls import path
from watchlist_app.api.v1.views.watchlist import movie_list, movie_detail


urlpatterns = [

    path("list/", movie_list, name="movie-list"),
    path("<int:movie_id>/",movie_detail, name='movie-detail')
]