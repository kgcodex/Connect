from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from api.models import Follow, Post
from api.serializers import PostFeedSerializer


@extend_schema(
    responses={
        200: PostFeedSerializer,
    }
)
@api_view(["GET"])
@permission_classes([IsAuthenticated])
def feed(request):
    userid = request.user.id

    # List of users, current user follows
    following_users = Follow.objects.filter(follower_id=userid).values_list(
        "user_id", flat=True
    )
    # Posts from users followed by current user
    posts = (
        Post.objects.filter(user__in=following_users)
        .select_related("user")
        .prefetch_related("comments", "likes_count")
        .order_by("-created_at")
    )

    serializer = PostFeedSerializer(posts, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
