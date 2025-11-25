from rest_framework import serializers


class SearchSerializer(serializers.Serializer):
    id = serializers.UUIDField()
    username = serializers.CharField()
    profile_pic_thumb = serializers.SerializerMethodField()

    def get_profile_pic_thumb(self, obj):
        try:
            return obj.profile_pic_thumb.url
        except:
            return None
