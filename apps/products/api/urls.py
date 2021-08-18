
from apps.products.api.views.general_views import MeasureUnitListAPIView, CategoryProductListAPIView, IndicatorListAPIView
from django.urls import path
urlpatterns = [
    path('measure_units/', MeasureUnitListAPIView.as_view(), name= 'measure_unit'),
    path('category_product/', CategoryProductListAPIView.as_view(), name= 'category_product'),
    path('indicator/', IndicatorListAPIView.as_view(), name= 'indicator'),
]