from rest_framework.response import Response
from rest_framework.views import APIView, Request

from django.shortcuts import get_object_or_404

from .models import Movie
from .serializers import MovieSerializer
from users.models import User

from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.authentication import JWTAuthentication

from .permissions import AuthPermissions

class MovieView( APIView ):

    authentication_classes = [JWTAuthentication]
    permission_classes = [AuthPermissions]

    def post( self, req:Request ) -> Response:

        req.data["added_by"] = req._user.email 

        movie = MovieSerializer(data=req.data)

        movie.is_valid(raise_exception=True)

        movie.save()
     
        return Response(movie.data,201)

    def get( self, req:Request ) -> Response:
        
        movie = Movie.objects.all()

        res_movies = MovieSerializer(movie, many=True)

        return Response(res_movies.data,200)


class MovieIdView( APIView ):

    authentication_classes = [JWTAuthentication]
    permission_classes = [AuthPermissions]

    def get( self, req:Request, movie_id: int ) -> Response:
        
        movie = get_object_or_404( Movie, id=movie_id)

        res_movie = MovieSerializer(movie)

        return Response(res_movie.data, 200)

    def delete( self, req:Request, movie_id: int ) -> Response:

        movie = get_object_or_404( Movie, id=movie_id)

        movie.delete()

        return Response(status=204)