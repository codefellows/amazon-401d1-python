from django.urls import path
from .views import SnackList, SnackDetail

urlpatterns = [
    path('', SnackList.as_view(), name="snack_list"),
    path('<int:pk>/', SnackDetail.as_view(), name="snack_detail"),
]
