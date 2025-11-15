from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from api.serializers import (
    TokenSerializer,
    UserDetailsSerializer,
    UserRegistrationSerializer,
)


# Health Check Endpoint
@api_view(["GET"])
@permission_classes([AllowAny])
def health_check(request):
    return Response({"status": "ok", "message": "API is healthy"})


# User Registration Endpoint
@extend_schema(
    request=UserRegistrationSerializer, responses={201: UserRegistrationSerializer}
)
@api_view(["POST"])
@permission_classes([AllowAny])
def register_user(request):
    serializer = UserRegistrationSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# User Login Endpoint
@extend_schema(request=TokenSerializer, responses={200: TokenSerializer})
@api_view(["POST"])
@permission_classes([AllowAny])
def login_user(request):
    serializer = TokenSerializer(data=request.data)

    if serializer.is_valid():
        return Response(serializer.validated_data, status=status.HTTP_200_OK)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# User Details Endpoint
@extend_schema(responses={200: UserDetailsSerializer})
@api_view(["GET"])
@permission_classes([IsAuthenticated])
def me_view(request):
    user = request.user

    serializer = UserDetailsSerializer(user, many=False)
    return Response(serializer.data)
