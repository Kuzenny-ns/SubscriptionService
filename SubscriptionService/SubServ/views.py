from django.shortcuts import render
from rest_framework import generics

# Create your views here.
from .models import User, Provider, Product, Service, Subscription
from .serializer import UserSerializer, ProviderSerializer, ProductSerializer, ServiceSerializer, SubscriptionSerializer

class UserAPIViev(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ProviderAPIViev(generics.ListAPIView):
    queryset = Provider.objects.all()
    serializer_class = ProviderSerializer

class ProductAPIViev(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ServiceAPIViev(generics.ListAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

class SubscriptionAPIViev(generics.ListAPIView):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer