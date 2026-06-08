from rest_framework import serializers


class TripOptimizationSerializer(
    serializers.Serializer
):

    start = serializers.CharField()

    destination = serializers.CharField()