from django.contrib import admin

# Register your models here.

from store.models import Brand,Tag,Size,Category,Product

admin.site.register(Brand)

admin.site.register(Tag)

admin.site.register(Size)

admin.site.register(Category)

admin.site.register(Product)

