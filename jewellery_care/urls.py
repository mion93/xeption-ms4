from django.urls import path
from . import views

urlpatterns = [
    path('', views.about, name='jewellery_care'),
]
