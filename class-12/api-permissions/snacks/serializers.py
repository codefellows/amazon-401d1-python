from rest_framework.serializers import ModelSerializer
from .models import Snack

class SnackSerializer(ModelSerializer):

    class Meta:
        model = Snack
        fields = ('id', 'name', 'purchaser')
