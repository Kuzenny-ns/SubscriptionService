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

class UserModel:
    def __init__(self, userID, userName, userEmail):
        self.userID = userID
        self.userName = userName
        self.userEmail = userEmail

class UserSerial(serializers.Serializer):
    userID = serializers.IntegerField()
    userName = serializers.CharField()
    userEmail = serializers.EmailField()

    def create(self, validated_data):
        return User.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.userID=validated_data.get("userID", instance.userID)
        instance.userName=validated_data.get("userName", instance.userName)
        instance.userlogin=validated_data.get("userlogin", instance.userlogin)
        instance.userEmail=validated_data.get("userEmail", instance.userEmail)
        instance.userPassword=validated_data.get("userPassword", instance.userPassword)
        instance.save()
        return instance

def encode():
    model = UserModel(10, 'Bob', 'example@gmail.com')
    model_sr = UserSerial(model)
    print(model_sr.data, type(model_sr.data), sep='\n')
    json = JSONRenderer().render(model_sr.data)
    print(json)