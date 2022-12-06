from rest_framework.views import APIView, Request
from rest_framework.response import Response

from django.shortcuts import get_object_or_404

from users.serializers import UserSerializer

from .serializers import CustomJWTSerializer

from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

class UserView( APIView ):

    def post( self, req: Request ) -> Response:
        
        user = UserSerializer(data=req.data)

        user.is_valid(raise_exception=True)

        user.save()

        return Response(user.data, 201)



class LoginJWTView(TokenObtainPairView):
    serializer_class = CustomJWTSerializer