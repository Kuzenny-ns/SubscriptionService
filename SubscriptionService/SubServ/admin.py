from django.contrib import admin

# Register your models here.
from .models import User, Provider, Product, Service, Subscription
admin.site.register(User)
admin.site.register(Provider)
admin.site.register(Product)
admin.site.register(Service)
admin.site.register(Subscription)

class ContactAdmin(admin.ModelAdmin):
    list_display = ('name')