from rest_framework import serializers

class DiagnosisSerializer(serializers.Serializer):
    diagnosis = serializers.CharField()

class DrugSerializer(serializers.Serializer):
    drug_info = serializers.CharField()