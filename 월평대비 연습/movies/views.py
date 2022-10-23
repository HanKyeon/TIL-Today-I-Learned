from django.shortcuts import render, get_list_or_404, get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from .models import Actor, Movie, Review
from .serializers import ActorListSerializer, ActorSerializer, MovieListSerializer, MovieSerializer, ReviewListSerializer, ReviewSerializer
from movies import serializers

# Create your views here.
@api_view(["GET"])
def actor_list(request):
    if request.method == "GET":
        actors = get_list_or_404(Actor)
        serializer = ActorListSerializer(actors, many=True)
        return Response(serializer.data)

@api_view(["GET"])
def actor_detail(request, actor_pk):
    if request.method == "GET":
        actor = get_object_or_404(Actor, pk=actor_pk)
        serializer = ActorSerializer(actor)
        print(serializer, '==========================')
        return Response(serializer.data)

@api_view(["GET"])
def movie_list(request):
    if request.method == "GET":
        movies = get_list_or_404(Movie)
        serializer = MovieListSerializer(movies, many=True)
        return Response(serializer.data)

@api_view(["GET"])
def movie_detail(request, movie_pk):
    if request.method == "GET":
        movie = get_object_or_404(Movie, pk=movie_pk)
        serializer = MovieSerializer(movie)
        return Response(serializer.data)

@api_view(["GET"])
def review_list(request):
    if request.method == "GET":
        reviews = get_list_or_404(Review)
        serializer = ReviewListSerializer(reviews, many=True)
        return Response(serializer.data)

@api_view(["GET", "PUT", "DELETE"])
def review_detail(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    if request.method == "GET":
        serializer = ReviewSerializer(review)
        return Response(serializer.data)
    if request.method == "PUT":
        serializer = ReviewSerializer(instance=review, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
    if request.method == "DELETE":
        review.delete()
        context = {
            'delete': f"review {review_pk} is deleted"
        }
        return Response(context, status=status.HTTP_204_NO_CONTENT)

@api_view(["POST"])
def create_review(request, movie_pk):
    if request.method == "POST":
        movie = get_object_or_404(Movie, pk=movie_pk)
        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(movie=movie)
            return Response(serializer.data)







