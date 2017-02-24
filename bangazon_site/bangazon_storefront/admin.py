from django.contrib import admin

# Register your models here.
from bangazon_storefront.models import *
admin.site.register(customer_model.Customer)
admin.site.register(order_model.Order)
admin.site.register(products_model.ProductsModel)
admin.site.register(product_types_model.ProductTypes)