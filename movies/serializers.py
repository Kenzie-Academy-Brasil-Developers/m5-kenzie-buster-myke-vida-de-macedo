from rest_framework import serializers
from .models import Raiting

from .models import Movie, MovieOrder
from users.models import User


class MovieSerializer( serializers.Serializer ):

    id = serializers.IntegerField(
        read_only=True
    )

    title = serializers.CharField(
        max_length=127
    )

    duration = serializers.CharField(
        max_length=10,
        default=None
    )

    rating = serializers.ChoiceField(
        choices=Raiting.choices,
        default=Raiting.G
    )

    synopsis = serializers.CharField(
        default=None
    )

    added_by = serializers.EmailField()

    def create(self, validated_data: dict):

        user_email = validated_data.pop("added_by")

        user = User.objects.get(email=user_email)

        movie = Movie.objects.create(**validated_data, added_by=user_email , user=user)

        return movie

class MovieOrderSerializer( serializers.Serializer ):

    id = serializers.IntegerField(read_only=True)

    buyed_at = serializers.DateTimeField(read_only=True)

    price = serializers.DecimalField(
        max_digits=8,
        decimal_places=2
    )

    buyed_by = serializers.SerializerMethodField()
    title = serializers.SerializerMethodField()

    user = serializers.IntegerField(
        write_only=True
    )

    movie = serializers.IntegerField(
        write_only=True
    )

    def get_buyed_by( self, obj:MovieOrder ):
        
        user = User.objects.get(pk=obj.user.id)

        return user.email

    def get_title( self, obj:MovieOrder ):

        movie = Movie.objects.get(pk=obj.movie.id)

        return movie.title
        

    def create(self, validated_data:MovieOrder):

        user = User.objects.get(pk=validated_data.pop("user"))
        movie = Movie.objects.get(pk=validated_data.pop("movie"))

        movie_order = MovieOrder.objects.create(**validated_data, user=user, movie=movie)

        return movie_order