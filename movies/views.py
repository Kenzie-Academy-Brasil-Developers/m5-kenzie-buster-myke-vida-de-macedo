from rest_framework.response import Response
from rest_framework.views import APIView, Request

from django.shortcuts import get_object_or_404

from .models import Movie
from .serializers import MovieSerializer, MovieOrderSerializer

from rest_framework_simplejwt.authentication import JWTAuthentication

from .permissions import AuthPermissions, TokenExistPermissions

from api.pagination import CustomPagePagination

class MovieView( APIView, CustomPagePagination ):

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

        result_page = self.paginate_queryset(movie, req, view=self)

        res_movies = MovieSerializer(result_page, many=True)

        return self.get_paginated_response(res_movies.data)


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

class MovieOrderIdView( APIView ):
    
    authentication_classes = [JWTAuthentication]
    permission_classes = [TokenExistPermissions]

    def post( self, req: Request, movie_id: int ) -> Response:

        get_object_or_404( Movie, id=movie_id)

        req.data["movie"] = movie_id
        req.data["user"] = req._user.id

        movie_order = MovieOrderSerializer(data=req.data)

        movie_order.is_valid(raise_exception=True)

        movie_order.save()

        return Response(movie_order.data, 201)