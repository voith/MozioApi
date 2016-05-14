from django.contrib.gis import admin
from models import Provider, ServiceArea


admin.site.register(Provider)
admin.site.register(ServiceArea, admin.OSMGeoAdmin)