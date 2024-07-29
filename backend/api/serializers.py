from rest_framework import serializers
from .models import DrugPrescriptionFileUpload

class DiagnosisSerializer(serializers.Serializer):
    diagnosis = serializers.CharField()

class DrugSerializer(serializers.Serializer):
    drug_info = serializers.CharField()

class FileUploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = DrugPrescriptionFileUpload
        fields = ('file', 'created','name')
