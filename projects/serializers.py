from rest_framework import serializers
from .models import Project

class ProjectSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()
    image_card = serializers.SerializerMethodField()

    class Meta:
        model = Project
        fields = '__all__'

    def get_image(self, obj):
        if not obj.image:
            return None
        request = self.context.get('request')
        return request.build_absolute_uri(obj.image.url)

    def get_image_card(self, obj):
        if not obj.image_card:
            return None
        request = self.context.get('request')
        return request.build_absolute_uri(obj.image_card.url)
