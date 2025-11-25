from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import OpenApiParameter, extend_schema, extend_schema_view
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from api.models import Comment
from api.serializers import GetCommentsSerializer, PostCommentsSerializer


@extend_schema_view(
    get=extend_schema(
        description="Retrieve comments for a specific post.",
        parameters=[
            OpenApiParameter(
                name="postid",
                type=OpenApiTypes.UUID,
                required=True,
                location=OpenApiParameter.QUERY,
                description="UUID of the post whose comments you want",
            )
        ],
        responses={
            200: GetCommentsSerializer(many=True),
        },
    ),
    post=extend_schema(
        description="Create a new comment",
        request=PostCommentsSerializer,
        responses={201: PostCommentsSerializer},
    ),
)
@api_view(["GET", "POST"])
@permission_classes([IsAuthenticated])
def comments(request):
    if request.method == "GET":
        postid = request.GET.get("postid")

        # Comments for the given post
        comments = Comment.objects.filter(post__id=postid).order_by("-created_at")
        if not comments.exists():
            return Response(
                {"message": "No comments found for this post."},
                status=status.HTTP_404_NOT_FOUND,
            )
        serializer = GetCommentsSerializer(comments, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    if request.method == "POST":
        serializer = PostCommentsSerializer(
            data=request.data, context={"request": request}
        )
        if serializer.is_valid():
            serializer.save()

            return Response(
                {"message": "Comment added successfully"},
                status=status.HTTP_201_CREATED,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
