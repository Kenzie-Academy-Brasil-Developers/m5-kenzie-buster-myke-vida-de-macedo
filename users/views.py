from rest_framework.views import APIView, Request
from rest_framework.response import Response

from django.shortcuts import get_object_or_404

from users.serializers import UserSerializer

class UserView( APIView ):
    def post( self, req: Request ) -> Response:
        
        user = UserSerializer(data=req.data)

        user.is_valid(raise_exception=True)

        user.save()

        return Response(user.data, 201)
