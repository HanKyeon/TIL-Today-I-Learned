from rest_framework import serializers
from .models import Actor, Movie, Review

class ActorListSerializer(serializers.ModelSerializer):

    class Meta():
        model = Actor
        fields = '__all__'

class MovieListSerializer(serializers.ModelSerializer):

    class Meta():
        model = Movie
        fields = "__all__"

class ReviewListSerializer(serializers.ModelSerializer):

    class Meta():
        model = Review
        fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):

    class Meta():
        model = Review
        fields = "__all__"
        read_only_fields = ('movie', )

class MovieSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True, read_only=True)
    r_t = serializers.SerializerMethodField(method_name='reviews_title_list')
    def reviews_title_list(self, obj):
        return obj.reviews.values('title')
    actor_names = serializers.SerializerMethodField(method_name='worked_actors')
    def worked_actors(self, obj):
        return obj.actors.values('name')

    class Meta():
        model = Movie
        fields = "__all__"
        read_only_fields = ("actors", )

class MovieTitleSerializer(serializers.ModelSerializer):

    class Meta():
        model = Movie
        fields = ('title',)
        read_only_fields=("actors",)

class ActorSerializer(serializers.ModelSerializer):
    movies = MovieSerializer(many=True, read_only=True)
    works22 = MovieTitleSerializer(many=True, read_only=True)
    works = serializers.SerializerMethodField(method_name='work')
    def work(self, obj):
        ret = []
        objlist = list(obj.movies.all())
        for i in objlist:
            ret.append(i.title)
        return ret

    class Meta():
        model = Actor
        fields = '__all__'

















