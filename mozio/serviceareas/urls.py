from django.conf.urls import url, include
from rest_framework import routers

from views import ProviderViewSet, ServiceAreaViewSet, ServiceAreaForPoint

router = routers.DefaultRouter()
router.register(r'provider', ProviderViewSet, 'provider')
router.register(r'servicearea', ServiceAreaViewSet, 'servicearea')

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),

    url(r'^search-servicearea/(?P<lat>(\-?\d+(\.\d+)?))/(?P<lng>(\-?\d+(\.\d+)?))/$',
        ServiceAreaForPoint.as_view()),
]
