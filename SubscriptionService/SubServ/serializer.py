from rest_framework import serializers
from rest_framework.renderers import JSONRenderer
from .models import User, Provider, Product, Service, Subscription

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("userID", "userName", "userEmail", "userlogin")

class ProviderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Provider
        #fields = ("providerID", "providerName", "providerDescription")
        fields = "__all__"

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        #fields = ("self.serviceID}", "serviceName", "serviceDescription", "servicePrice", "serviceFrequncy", "serviceCategory")
        fields = "__all__"

class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = ("subscriptionID", "subscriptionTimeSpan", "subscriptionService", "subscriptionSubscriber")