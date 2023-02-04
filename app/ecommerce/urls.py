from django.urls import path, include

from .views import *


urlpatterns = [
    path('api/v1/products', ProductAPIList.as_view(), name='products'),
]