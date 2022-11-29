from django.db import models

# Create your models here.
class Product(models.Model):
    productID = models.AutoField(primary_key=True)
    productType = models.CharField(max_length=50)
    productFormFactor = models.CharField(max_length=50, blank=True)
    
    def __str__(self):
        return f"{self.productID}" f"{self.productType}" f"{self.productFormFactor}"




class Service(models.Model):
    serviceID = models.AutoField(primary_key=True)
    serviceName = models.CharField(max_length=50)
    serviceDescription = models.CharField(max_length=350)
    servicePhotoURL = models.CharField(max_length=1000)
    serviceProduct = models.ForeignKey(Product, on_delete=models.CASCADE) 
    serviceCategory = models.CharField(max_length=50, blank=True)
    servicePrice = models.DecimalField(max_digits=6, decimal_places=2)
    serviceFrequncy = models.IntegerField()
    
    def __str__(self):
        return f"{self.serviceID}" f"{self.serviceName}" f"{self.serviceDescription}" f"{self.servicePrice}" f"{self.serviceFrequncy}"




class User(models.Model):
    userID = models.AutoField(primary_key=True)
    userName = models.CharField(max_length=50)
    userlogin = models.CharField(max_length=50)
    userEmail = models.EmailField(db_index=True)
    userPassword = models.CharField(max_length=50)
    
    def __str__(self):
        return f"{self.userID}" f"{self.userName}" f"{self.userEmail}" f"{self.userlogin}"




class Subscription(models.Model):
    subscriptionID = models.AutoField(primary_key=True)
    subscriptionTimeSpan = models.DateField()
    subscriptionAddress = models.CharField(max_length=50)
    subscriptionService = models.ForeignKey(Service, on_delete=models.CASCADE)
    subscriptionSubscriber = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.subscriptionID}" f"{self.subscriptionTimeSpan}" f"{self.subscriptionService}" f"{self.subscriptionSubscriber}"




class Provider(models.Model):
    providerID = models.AutoField(primary_key=True)
    providerName = models.CharField(max_length=50)
    providerDescription = models.CharField(max_length=350)
    providerService = models.ForeignKey(Service, on_delete=models.CASCADE)
    providerUser = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.providerID}" f"{self.providerName}" f"{self.providerDescription}"