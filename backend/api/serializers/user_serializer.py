# Serializer for User Details
from rest_framework import serializers

from api.models import User


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


# Serializer for updating User Details
class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "name",
            "bio",
            "dob",
            "profile_pic",
        )

    def update(self, instance, validated_data):
        for field, value in validated_data.items():
            setattr(instance, field, value)
        instance.save()

        return instance
