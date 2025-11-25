from rest_framework import serializers

from api.models import Post


class PostFeedSerializer(serializers.Serializer):
    postid = serializers.UUIDField(source="id", read_only=True)
    username = serializers.CharField(source="user.username", read_only=True)
    profile_pic = serializers.SerializerMethodField()
    content = serializers.CharField(read_only=True)
    mediaURL = serializers.SerializerMethodField()
    comments_count = serializers.SerializerMethodField()
    likes_count = serializers.SerializerMethodField()

    def get_profile_pic(self, obj):
        try:
            return obj.user.profile_pic_thumb.url
        except Exception:
            return None

    def get_mediaURL(self, obj):
        try:
            return obj.media_url.url
        except Exception:
            return None

    def get_comments_count(self, obj):
        return obj.comments.count()

    def get_likes_count(self, obj):
        return obj.likes_count.count if hasattr(obj, "likes_count") else 0


class CreatePostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ["content", "media_url"]

    def create(self, validated_data):
        user = self.context["request"].user
        return Post.objects.create(user=user, **validated_data)
