from rest_framework import serializers
from .models import Raiting

from .models import Movie
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

