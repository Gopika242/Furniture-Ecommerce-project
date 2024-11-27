from django.contrib import admin

# Register your models here.
from FurnitureApp.models import CategoryDb,ProductDb

admin.site.register(CategoryDb)
admin.site.register(ProductDb)