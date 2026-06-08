from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import TripOptimizeSerializer


class TripOptimizeView(GenericAPIView):
    serializer_class = TripOptimizeSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        return Response({
            "start": serializer.validated_data["start"],
            "destination": serializer.validated_data["destination"],
            "message": "Route optimization coming next"
        })