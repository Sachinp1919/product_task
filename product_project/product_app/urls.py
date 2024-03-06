from django.urls import path
from .views import ProductGetAPI, ProductDetailsAPI, ProductCreateAPI


urlpatterns = [
    path('product/', ProductGetAPI.as_view()),
    path('create/',ProductCreateAPI.as_view()),
    path('product/<int:pk>/', ProductDetailsAPI.as_view())
]