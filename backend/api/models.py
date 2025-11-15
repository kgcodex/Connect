import uuid

from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)
from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill

from api.utils.rename_file import UploadWithUUIDFilename
from api.utils.validate_age import validate_age


# Custom User Manager
class UserManager(BaseUserManager):
    def create_user(self, email, username, name, password=None, **extra_fields):
        """
        Create a User with Email and Password
        """
        if not email:
            raise ValueError("Email is required.")
        if not username:
            raise ValueError("Username is required.")

        email = self.normalize_email(email)
        user = self.model(email=email, username=username, name=name, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(unique=True, null=False)

    username = models.CharField(max_length=100, unique=True, null=False)
    name = models.CharField(max_length=100, null=False)

    bio = models.TextField(null=True, blank=True)
    dob = models.DateField(validators=[validate_age], null=False, blank=False)

    profile_pic = models.ImageField(
        upload_to=UploadWithUUIDFilename("profile_pics/"), null=True, blank=True
    )
    profile_pic_thumb = ImageSpecField(
        source="profile_pic",
        processors=[ResizeToFill(32, 32)],
        format="JPEG",
        options={"quality": 80},
    )

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    objects = UserManager()
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username", "name"]

    def __str__(self):
        return self.username


class Post(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="posts",
        related_query_name="posts",
    )
    content = models.TextField(null=True, blank=True)
    media_url = models.FileField(
        upload_to=UploadWithUUIDFilename("post_media/"), null=True, blank=True
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        indexes = [
            models.Index(fields=["user"]),
        ]


class Comment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name="comments",
        related_query_name="comments",
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="comments",
        related_query_name="comments",
    )
    content = models.TextField(null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        indexes = [
            models.Index(fields=["post"]),
            models.Index(fields=["user"]),
        ]


class Like(models.Model):
    post = models.OneToOneField(
        Post,
        on_delete=models.CASCADE,
        related_name="likes_count",
        related_query_name="likes_count",
    )
    count = models.PositiveIntegerField(default=0)


class Follow(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="followers",
        related_query_name="followers",
    )
    follower = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="following",
        related_query_name="following",
    )

    class Meta:
        unique_together = ("user", "follower")
        indexes = [
            models.Index(fields=["user"]),
            models.Index(fields=["follower"]),
        ]
