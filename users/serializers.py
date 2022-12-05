from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from users.models import User

class UserSerializer( serializers.Serializer ):

    id = serializers.IntegerField(read_only=True)

    username = serializers.CharField(
        max_length=20,
        validators=[
            UniqueValidator(
                queryset=User.objects.all(),
                message="username already taken."
            )
        ]
    )

    email = serializers.EmailField(
        max_length=127,
        validators=[
            UniqueValidator(
                queryset=User.objects.all(),
                message="email already registered."
            )
        ]
    )

    password = serializers.CharField(
        write_only=True
    )

    first_name = serializers.CharField(
        max_length=50
    )

    last_name = serializers.CharField(
        max_length=50
    )

    birthdate = serializers.DateField(
        default=None
    )

    is_employee = serializers.BooleanField(
        default=False
    )

    is_superuser = serializers.BooleanField(
        read_only=True
    )
    
    def create(self, validated_data: dict ) :
        
        if "is_employee" in validated_data and validated_data["is_employee"]:
            user_data = User.objects.create_superuser(**validated_data)

            return user_data

        user_data = User.objects.create_user(**validated_data)

        return user_data