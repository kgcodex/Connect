from rest_framework import serializers

from api.models import Follow


class FollowingListSerializer(serializers.Serializer):
    username = serializers.CharField(source="user.username", read_only=True)
    profile_pic_thumb = serializers.SerializerMethodField()

    def get_profile_pic_thumb(self, obj):
        try:
            return obj.user.profile_pic_thumb.url
        except Exception:
            return None


class FollowerListSerializer(serializers.Serializer):
    username = serializers.CharField(source="follower.username", read_only=True)
    profile_pic_thumb = serializers.SerializerMethodField()

    def get_profile_pic_thumb(self, obj):
        try:
            return obj.follower.profile_pic_thumb.url
        except Exception:
            return None


class AddFollowingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Follow
        fields = ["user"]

    def create(self, validated_data):
        follower = self.context["request"].user
        user_to_follow = validated_data["user"]

        if follower == user_to_follow:
            raise serializers.ValidationError("You cannot follow youself.")

        return Follow.objects.create(
            user=user_to_follow,
            follower=follower,
        )
