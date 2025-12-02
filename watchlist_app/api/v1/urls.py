from django.urls import path
from watchlist_app.api.v1.views.watchlist import MovieListAPIView, MovieDetailsAPIView, PlatformListsAPIView,PlatformDetailAPIView

app_name = 'watchlist_app'
urlpatterns =[
    path("list/", MovieListAPIView.as_view(),name='movie-list'),
    path("<int:pk>/", MovieDetailsAPIView.as_view(),name='movie-detail'),
    path("platform/", PlatformListsAPIView.as_view(),name='platform-list'),
    path("platform/<int:platform_id>/", PlatformDetailAPIView.as_view(),name='platform-detail'),

]