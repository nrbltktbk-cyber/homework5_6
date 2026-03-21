from django.contrib import admin
from .models import Product, SerialNumber, ReviewProduct, Tag

admin.site.register(Product)
admin.site.register(SerialNumber)
admin.site.register(ReviewProduct)
admin.site.register(Tag)
