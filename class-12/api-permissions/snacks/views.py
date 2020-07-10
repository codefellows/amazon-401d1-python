from django.shortcuts import render

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from .models import Snack
from .serializers import SnackSerializer
from .permissions import IsPurchaserOrReadOnly

class SnackList(ListCreateAPIView):
    queryset = Snack.objects.all()
    serializer_class = SnackSerializer
    permission_classes = (IsPurchaserOrReadOnly, )

class SnackDetail(RetrieveUpdateDestroyAPIView):
    queryset = Snack.objects.all()
    serializer_class = SnackSerializer
    permission_classes = (IsPurchaserOrReadOnly, )
