from drf_yasg import openapi
from drf_yasg.views import get_schema_view

schema_view = get_schema_view(
   openapi.Info(
      title="EatTop API",
      default_version='v1',
      description="EatTop API description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@eat.top"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
)
