from django.contrib import admin
from .models import *

admin.site.register(Shop)
admin.site.register(Complaint)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress)