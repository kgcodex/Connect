from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import OpenApiParameter, extend_schema
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from api.models import User
from api.serializers import SearchSerializer


@extend_schema(
    parameters=[
        OpenApiParameter(
            name="username",
            type=OpenApiTypes.STR,
            required=True,
            location=OpenApiParameter.QUERY,
            description="Username to search for",
        )
    ],
    responses={
        200: SearchSerializer(many=True),
    },
)
@api_view(["GET"])
@permission_classes([IsAuthenticated])
def search_users(request):
    """
    Search for user by username.
    """
    username = request.GET.get("username", "").strip()

    if not username:
        return Response(
            {"error": "Username is required"}, status=status.HTTP_400_BAD_REQUEST
        )

    user = User.objects.filter(username__icontains=username)

    if not user.exists():
        return Response({"error": "User not found."}, status=status.HTTP_404_NOT_FOUND)

    serializer = SearchSerializer(user, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
