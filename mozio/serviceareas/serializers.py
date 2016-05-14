from rest_framework import serializers
from rest_framework_gis.serializers import GeoFeatureModelSerializer

from models import Provider, ServiceArea


class ProviderSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Provider
        fields = ('id', 'name', 'email', 'phone_number', 'language', 'currency')


class ServiceAreaSerializer(GeoFeatureModelSerializer):

    class Meta:
        model = ServiceArea
        geo_field = 'poly'
        fields = ('name', 'provider', 'price')


class ServiceAreaQuerySerializer(serializers.HyperlinkedModelSerializer):

    provider = serializers.StringRelatedField()

    class Meta:
        model = ServiceArea
        fields = ('name', 'provider', 'price')
