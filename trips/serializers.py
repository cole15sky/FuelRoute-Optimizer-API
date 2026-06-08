from rest_framework import serializers


class TripOptimizeSerializer(serializers.Serializer):
    start = serializers.CharField()
    destination = serializers.CharField()