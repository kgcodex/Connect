from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from api.v1.views import *

urlpatterns = [
    # Auth Endpoints
    path("register/", register_user),
    path("login/", login_user),
    path("refresh/", TokenRefreshView.as_view()),
    # Profile Endpoint
    path("profile/", profile),
    # Feed Endpoint
    path("feed/", feed),
    # Search Users Endpoint
    path("search/", search_users),
    # Comments Endpoint
    path("comments/", comments),
    # Create or delete post
    path("post/", post_view),
    # All post of a user
    path("all_posts/", all_posts),
    # Manage follower and followee
    path("following/", following),
    path("follower/", followed_by),
]
