from django.urls import path
from .views import SnacksListView

urlpatterns = [
    path('', SnacksListView.as_view(), name='snacks_list')
]

