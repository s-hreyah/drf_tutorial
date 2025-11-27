from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from watchlist_app.api.v1.serializers.watchlist import WatchListSerializer
from watchlist_app.models import Movie


# Create your views here.
@api_view(['GET','POST'])
def movie_list(request):
    if request.method.lower()=='get':
        movies = Movie.objects.all()
    # data={
    #     'movies':list(movies.values())
    # }
        serializer= WatchListSerializer(movies,many=True)
        return Response(serializer.data)

    if request.method.lower()=='post':
        serializer=WatchListSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


@api_view(['GET','PUT','PATCH','DELETE'])
def movie_detail(request, movie_id):
    if request.method.lower()=='get':
        movie = Movie.objects.get(id=movie_id)
    # data={'name':movie.name,'description':movie.description,'active':movie.active}
        serializer=WatchListSerializer(movie)
        return Response(serializer.data)

    if request.method.lower()=='put':
        movie=Movie.objects.get(id=movie_id)
        serializer=WatchListSerializer(movie,data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    if request.method.lower()=='delete':
        movie=Movie.objects.get(id=movie_id)
        movie.delete()
        return Response("Deleted Successfully")


    if request.method.lower()=='patch':
        movie=Movie.objects.get(id=movie_id)
        serializer=WatchListSerializer(movie,data=request.data,partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
