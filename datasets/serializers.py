from rest_framework import serializers
from .models import Dataset, DatasetVersion, DatasetMetadata

class MetadataSerializer(serializers.ModelSerializer):
    class Meta:
        model = DatasetMetadata
        fields = ['key', 'value']

class VersionSerializer(serializers.ModelSerializer):
    class Meta:
        model = DatasetVersion
        fields = '__all__'

class DatasetSerializer(serializers.ModelSerializer):
    metadata = MetadataSerializer(many=True, read_only=True)
    versions = VersionSerializer(many=True, read_only=True)

    class Meta:
        model = Dataset
        fields = '__all__'