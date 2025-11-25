from django.db import IntegrityError
from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import OpenApiParameter, extend_schema, extend_schema_view
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from api.models import Follow, User
from api.serializers import (
    AddFollowingSerializer,
    FollowerListSerializer,
    FollowingListSerializer,
)


@extend_schema_view(
    get=extend_schema(
        description="Get the list or count of the people you follow",
        parameters=[
            OpenApiParameter(
                name="query",
                type=OpenApiTypes.STR,
                required=True,
                location=OpenApiParameter.QUERY,
                enum=["list", "count"],
            ),
        ],
        responses={200: FollowingListSerializer},
    ),
    post=extend_schema(
        description="Follow another user",
        request=AddFollowingSerializer,
    ),
)
@api_view(["GET", "POST"])
@permission_classes([IsAuthenticated])
def following(request):
    if request.method == "GET":
        query = request.GET.get("query")

        if not query:
            return Response(
                {"message": "query parameter is required. Use 'list' or 'count'."},
                status=status.HTTP_400_BAD_REQUEST,
            )
        # Get current user
        user = request.user

        if query == "list":
            # All the user who are followed by current user
            follows = Follow.objects.filter(follower=user)

            serializer = FollowingListSerializer(follows, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

        if query == "count":
            follows_count = Follow.objects.filter(follower=user).count()
            return Response({"count": follows_count}, status=status.HTTP_200_OK)

        return Response(
            {"error": "Only list, count are acceptable."},
            status=status.HTTP_400_BAD_REQUEST,
        )

    if request.method == "POST":
        # Get User id from Username
        user = request.data.get("username")

        try:
            userid = User.objects.get(username=user).id
        except User.DoesNotExist:
            return Response(
                {"error": "user does not exist"}, status=status.HTTP_400_BAD_REQUEST
            )

        serializer = AddFollowingSerializer(
            data={"user": userid}, context={"request": request}
        )
        if serializer.is_valid():
            try:
                serializer.save()
                return Response(
                    {"message": "Successfully Followed"}, status=status.HTTP_201_CREATED
                )
            except IntegrityError:
                return Response(
                    {"message": "You already follow this user."},
                    status=status.HTTP_400_BAD_REQUEST,
                )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@extend_schema(
    description="Get list of all the user who follows current user.",
    parameters=[
        OpenApiParameter(
            name="query",
            type=OpenApiTypes.STR,
            required=True,
            location=OpenApiParameter.QUERY,
            enum=["list", "count"],
        ),
    ],
    responses={
        200: FollowerListSerializer,
    },
)
@api_view(["GET"])
@permission_classes([IsAuthenticated])
def followed_by(request):
    query = request.GET.get("query")
    user = request.user

    if query == "list":
        followedby = Follow.objects.filter(user=user)

        serializer = FollowerListSerializer(followedby, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    if query == "count":
        followedby_count = Follow.objects.filter(user=user).count()
        return Response({"count": followedby_count}, status=status.HTTP_200_OK)

    return Response(
        {"error": "Only list, count are acceptable."},
        status=status.HTTP_400_BAD_REQUEST,
    )
