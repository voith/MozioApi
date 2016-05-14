from django.contrib.gis.geos import Point
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response

from models import Provider, ServiceArea
from serializers import ProviderSerializer, ServiceAreaSerializer, ServiceAreaQuerySerializer


class ProviderViewSet(viewsets.ModelViewSet):
    """
    API Endpoint for providers ordered by id to view and modify.
    """

    queryset = Provider.objects.all().order_by('id')
    serializer_class = ProviderSerializer
    http_method_names = ['get', 'post', 'update', 'delete']


class ServiceAreaViewSet(viewsets.ModelViewSet):
    """
    API Endpoint for servicearea ordered by id to view and modify.
    """

    queryset = ServiceArea.objects.all().order_by('id')
    serializer_class = ServiceAreaSerializer
    http_method_names = ['get', 'post', 'update', 'delete']


class ServiceAreaForPoint(APIView):
    """
    GET all servicearea's that have the same latitude and longitude
    """

    def get(self, request, lat, lng):
        point = Point(float(lng), float(lat))
        servicearea_objs = ServiceArea.objects.filter(poly__contains=point)
        serializer = ServiceAreaQuerySerializer(servicearea_objs, many=True)
        return Response(serializer.data)
