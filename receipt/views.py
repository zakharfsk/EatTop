from rest_framework import generics

from .models import Check
from .serializers import CheckSerializer


class CheckGenericAPIView(generics.CreateAPIView):
    queryset = Check.objects.all()
    serializer_class = CheckSerializer
