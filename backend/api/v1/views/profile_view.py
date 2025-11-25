from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import OpenApiParameter, extend_schema, extend_schema_view
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from api.models import User
from api.serializers import UserDetailsSerializer, UserUpdateSerializer


@extend_schema_view(
    get=extend_schema(
        parameters=[
            OpenApiParameter(
                name="username",
                type=OpenApiTypes.STR,
                required=False,
                location=OpenApiParameter.QUERY,
                description="Username of the profile to retrieve",
            )
        ],
        responses={200: UserDetailsSerializer},
    ),
    patch=extend_schema(
        request=UserUpdateSerializer,
        responses={200: UserDetailsSerializer},
        description="Update own profile details",
    ),
    delete=extend_schema(
        description="Delete your own profile",
    ),
)
@api_view(["GET", "PATCH", "DELETE"])
@permission_classes([IsAuthenticated])
def profile(request):
    if request.method == "GET":
        username = request.GET.get("username", "").strip()

        if username:
            try:
                user = User.objects.get(username=username)
            except User.DoesNotExist:
                return Response(
                    {"message": "User not found"}, status=status.HTTP_404_NOT_FOUND
                )
        else:
            user = request.user

        serializer = UserDetailsSerializer(user)

        return Response(serializer.data, status=status.HTTP_200_OK)

    if request.method == "PATCH":
        user = request.user
        serializer = UserUpdateSerializer(user, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()

            return Response(UserDetailsSerializer(user).data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == "DELETE":
        user = request.user
        user.delete()

        return Response(
            {"message": "User deleted successfully"}, status=status.HTTP_200_OK
        )
