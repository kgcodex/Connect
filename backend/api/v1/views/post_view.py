import os

from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import OpenApiParameter, extend_schema, extend_schema_view
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from api.models import Post, User
from api.serializers import CreatePostSerializer, PostFeedSerializer


@extend_schema_view(
    post=extend_schema(request=CreatePostSerializer, description="Create a new post"),
    delete=extend_schema(
        parameters=[
            OpenApiParameter(
                name="postid",
                type=OpenApiTypes.UUID,
                required=True,
                location=OpenApiParameter.QUERY,
                description="UUID of the Post",
            )
        ],
        description="Delete your post",
    ),
)
@api_view(["POST", "DELETE"])
@permission_classes([IsAuthenticated])
def post_view(request):
    if request.method == "POST":
        serializer = CreatePostSerializer(
            data=request.data, context={"request": request}
        )

        if serializer.is_valid():
            post = serializer.save()
            response_data = {
                "message": "Post created successfully",
            }

            if os.getenv("DEBUG"):
                response_data["postid"] = str(post.id)

            return Response(
                response_data,
                status=status.HTTP_201_CREATED,
            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == "DELETE":
        postid = request.GET.get("postid")

        if not postid:
            return Response(
                {"error": "postid query parameter is required"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        try:
            post = Post.objects.get(id=postid)
        except Post.DoesNotExist:
            return Response(
                {"error": "Post not found"}, status=status.HTTP_404_NOT_FOUND
            )

        if post.user == request.user:
            post.delete()

            return Response(
                {"message": "Post deleted successfully"}, status=status.HTTP_200_OK
            )

        return Response(
            {"message": "You are not authorized for this"},
            status=status.HTTP_403_FORBIDDEN,
        )


@extend_schema(
    parameters=[
        OpenApiParameter(
            name="username",
            type=OpenApiTypes.STR,
            required=False,
            location=OpenApiParameter.QUERY,
            description="Username of the profile whose post should be fetched.",
        ),
    ],
    responses={
        200: PostFeedSerializer,
    },
)
@api_view(["GET"])
@permission_classes([IsAuthenticated])
def all_posts(request):
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

    posts = (
        Post.objects.filter(user=user)
        .select_related("user")
        .select_related("likes_count")
        .prefetch_related("comments")
        .order_by("-created_at")
    )

    serializer = PostFeedSerializer(posts, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
