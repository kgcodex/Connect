from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from .views import health_check, login_user, me_view, register_user

urlpatterns = [
    # Health Check Endpoint
    path("health_check/", health_check),
    # Auth Endpoints
    path("register/", register_user),
    path("login/", login_user),
    path("refresh/", TokenRefreshView.as_view()),
    # User Details Endpoint
    path("me/", me_view),
]
