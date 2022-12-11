from rest_framework.views import APIView, Request
from rest_framework.response import Response

from django.shortcuts import get_object_or_404

from .models import User

from users.serializers import UserSerializer

from .serializers import CustomJWTSerializer

from rest_framework_simplejwt.views import TokenObtainPairView
from .permissions import UserPermission
from rest_framework_simplejwt.authentication import JWTAuthentication

from movies.permissions import TokenExistPermissions

class UserView( APIView ):

    def post( self, req: Request ) -> Response:
        
        user = UserSerializer(data=req.data)

        user.is_valid(raise_exception=True)

        user.save()

        return Response(user.data, 201)

class UserIdView( APIView ):

    authentication_classes = [JWTAuthentication]
    permission_classes = [TokenExistPermissions, UserPermission]

    def get( self, req: Request, user_id:int ) -> Response:

        user = get_object_or_404(User, id=user_id)
        
        self.check_object_permissions(req, user)

        res_user = UserSerializer(user)

        return Response(res_user.data)

class LoginJWTView(TokenObtainPairView):
    serializer_class = CustomJWTSerializer