from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from api.serializers import TokenSerializer, UserRegistrationSerializer


# User Registration Endpoint
@extend_schema(
    request=UserRegistrationSerializer,
    responses={
        201: UserRegistrationSerializer,
    },
)
@api_view(["POST"])
@permission_classes([AllowAny])
def register_user(request):
    """
    Register a new user.
    """
    serializer = UserRegistrationSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.validated_data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# User Login Endpoint
@extend_schema(
    request=TokenSerializer,
)
@api_view(["POST"])
@permission_classes([AllowAny])
def login_user(request):
    """
    Login user and return JWT Tokens.
    """
    serializer = TokenSerializer(data=request.data)

    if serializer.is_valid():
        return Response(serializer.validated_data, status=status.HTTP_200_OK)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
