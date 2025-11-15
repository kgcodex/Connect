from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from api.models import User


# Serializer for Token
class TokenSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Custom claims
        token["username"] = user.username
        token["email"] = user.email
        token["user_id"] = str(user.id)

        return token


# Serializer for User Registration
class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, min_length=8)

    class Meta:
        model = User
        fields = ("email", "username", "name", "password", "dob")

    def create(self, validated_data):
        user = User.objects.create_user(
            email=validated_data["email"],
            username=validated_data["username"],
            name=validated_data["name"],
            password=validated_data["password"],
            dob=validated_data["dob"],
        )
        return user


# Serializer for User Details
class UserDetailsSerializer(serializers.ModelSerializer):
    profile_pic_thumb_url = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = (
            "id",
            "email",
            "username",
            "name",
            "bio",
            "dob",
            "profile_pic",
            "profile_pic_thumb_url",
        )

    def get_profile_pic_thumb_url(self, obj):
        if obj.profile_pic_thumb:
            return obj.profile_pic_thumb.url
        return None
