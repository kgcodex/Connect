# Health Check Endpoint
# @api_view(["GET"])
# @permission_classes([AllowAny])
# def health_check(request):
#     return Response({"status": "ok", "message": "API is healthy"})


# User Registration Endpoint
# @extend_schema(
#     request=UserRegistrationSerializer,
#     responses={
#         201: UserRegistrationSerializer,
#         400: OpenApiResponse(response=OpenApiTypes.OBJECT),
#     },
# )
# @api_view(["POST"])
# @permission_classes([AllowAny])
# def register_user(request):
#     serializer = UserRegistrationSerializer(data=request.data)

#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)

#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# User Login Endpoint
# @extend_schema(request=TokenSerializer, responses={200: TokenSerializer})
# @api_view(["POST"])
# @permission_classes([AllowAny])
# def login_user(request):
#     """Login user and return JWT Tokens"""
#     serializer = TokenSerializer(data=request.data)

#     if serializer.is_valid():
#         return Response(serializer.validated_data, status=status.HTTP_200_OK)

#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# User Details Endpoint
# @extend_schema(responses={200: UserDetailsSerializer})
# @api_view(["GET"])
# @permission_classes([IsAuthenticated])
# def me_view(request):
#     user = request.user
#     print(user.id)
#     serializer = UserDetailsSerializer(user, many=False)
#     return Response(serializer.data)


# @api_view(["GET"])
# def feed(request):
#     userid = request.user.id

#     # List of users, current user follows
#     following_users = Follow.objects.filter(follower=userid).values_list(
#         "user_id", flat=True
#     )
#     # Posts from users followed by current user
#     posts = (
#         Post.objects.filter(user__in=following_users)
#         .select_related("user")
#         .prefetch_related("comments", "likes_count")
#         .order_by("-created_at")
#     )

#     serializer = PostFeedSerializer(posts, many=True)
#     return Response(serializer.data)


# @api_view(["GET"])
# def search_users(request):
#     username = request.GET.get("username", "").strip()

#     if not username:
#         return Response({"error": "Username is required"})

#     user = User.objects.filter(username__icontains=username)

#     if not user.exists():
#         return Response({"error": "User not found."})

#     serializer = SearchSerializer(user, many=True)
#     return Response(serializer.data)


# @api_view(["GET", "POST"])
# def comments(request):
#     if request.method == "GET":
#         postid = request.GET.get("postid")

#         # Comments for the given post
#         comments = Comment.objects.filter(post__id=postid).order_by("-created_at")
#         if not comments.exists():
#             return Response({"message": "No comments found for this post."})
#         serializer = GetCommentsSerializer(comments, many=True)

#         return Response(serializer.data)

#     if request.method == "POST":
#         serializer = PostCommentsSerializer(
#             data=request.data, context={"request": request}
#         )
#         if serializer.is_valid():
#             serializer.save()

#             return Response(
#                 {"message": "Comment added successfully"},
#                 status=status.HTTP_201_CREATED,
#             )
