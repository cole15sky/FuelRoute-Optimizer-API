from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import TripOptimizeSerializer
from fuel.services.trip_service import TripService


class TripOptimizeView(GenericAPIView):

    serializer_class = TripOptimizeSerializer

    def post(self, request):

        serializer = self.get_serializer(
            data=request.data
        )

        serializer.is_valid(
            raise_exception=True
        )

        result = TripService.optimize_trip(
            serializer.validated_data["start"],
            serializer.validated_data["destination"],
        )

        return Response(
            result,
            status=status.HTTP_200_OK,
        )