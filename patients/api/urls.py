from django.conf.urls import url
from django.urls import path, include
from .views import PatientsViewSet, DoctorsViewSet, AppointmentsViewSet, InvoicesViewSet
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'patients', PatientsViewSet)
router.register(r'doctors', DoctorsViewSet)
router.register(r'appointments', AppointmentsViewSet)
router.register(r'invoices', InvoicesViewSet)

schema_view = get_schema_view(
    openapi.Info(
        title="Patient Management System API",
        default_version='v1',
        description="Patient Management System API",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="curewellhomeo101@gmail.com"),
        license=openapi.License(name="MIT License"),
    ),
    public=False,
    permission_classes=(permissions.IsAuthenticated, ),
)

urlpatterns = [
    url(r'^swagger(?P<format>\.json|\.yaml)$',
        schema_view.without_ui(cache_timeout=0),
        name='schema-json'),
    url(r'^swagger/$',
        schema_view.with_ui('swagger', cache_timeout=0),
        name='schema-swagger-ui'),
    url(r'^redoc/$',
        schema_view.with_ui('redoc', cache_timeout=0),
        name='schema-redoc'),
    path('', include(router.urls)),
]