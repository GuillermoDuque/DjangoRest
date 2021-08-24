from apps.products.models import MeasureUnit, CategoryProduct, Indicator, Product
from django.contrib import admin


myModels = [MeasureUnit, CategoryProduct, Indicator, Product]  # iterable list
admin.site.register(myModels)