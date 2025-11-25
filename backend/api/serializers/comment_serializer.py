from rest_framework import serializers

from api.models import Comment


class GetCommentsSerializer(serializers.Serializer):
    username = serializers.CharField(source="user.username", read_only=True)
    profile_pic_thumb = serializers.SerializerMethodField()
    content = serializers.CharField()

    def get_profile_pic_thumb(self, obj):
        try:
            return obj.user.profile_pic_thumb.url
        except Exception:
            return None


class PostCommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ["post", "content"]

    def create(self, validated_data):
        user = self.context["request"].user
        return Comment.objects.create(user=user, **validated_data)
