from rest_framework import serializers

from .models import File

class UploadSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = File
        fields = ['file']

        def create(self, validated_data):
            return File.objects.create(**validated_data)
        
class FileSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = File
        fields = '__all__'
