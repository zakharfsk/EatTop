from django.conf.urls.static import static
from django.urls import path

from EatTop import settings
from . import views

urlpatterns = [
    path('check/', views.CheckGenericAPIView.as_view()),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
