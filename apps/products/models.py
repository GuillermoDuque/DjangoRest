from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields.related import ForeignObject
from simple_history.models import HistoricalRecords
from apps.base.models import BaseModel
# Create your models here.

class MeasureUnit(BaseModel):
    """Model definition for MeasureUnit."""

    description = models.CharField('Description', max_length=50, blank=False, null=False, unique = True)
    historical = HistoricalRecords()

    @property
    def _history_user(self):
        return self.changed_by
    
    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value
    
    class Meta:
        """Meta definition for MeasureUnit."""

        verbose_name = 'MeasureUnit'
        verbose_name_plural = 'MeasureUnits'


    def __str__(self):
        """Unicode representation of MeasureUnit."""
        return self.description


class CategoryProduct(BaseModel):
    """Model definition for CategoryProduct."""

    # TODO: Define fields here
    description = models.CharField('Description', max_length=50, unique=True, null=False, blank= False)
    historical = HistoricalRecords()
    @property
    def _history_user(self):
        return self.changed_by
    
    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value

    class Meta:
        """Meta definition for CategoryProduct."""

        verbose_name = 'CategoryProduct'
        verbose_name_plural = 'CategoryProducts'

    def __str__(self):
        return self.description

class Indicator(BaseModel):
    """Model definition for Indicator."""

    # TODO: Define fields here
    descount_value = models.PositiveSmallIntegerField(default=0)
    category_product = models.ForeignKey(CategoryProduct,on_delete=models.CASCADE, verbose_name='offer indicator')
    historical = HistoricalRecords()

    @property
    def _history_user(self):
        return self.changed_by
    
    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value

    class Meta:
        """Meta definition for Indicator."""

        verbose_name = 'Indicator'
        verbose_name_plural = 'Indicators'

    def __str__(self):
        """Unicode representation of Indicator."""
        return f'category\'s offer{self.category_product} : {self.descount_value}%'

class Product(BaseModel):
    """Model definition for Product."""
    name = models.CharField('Product name', max_length=150, unique=True, null=False, blank=False)
    description = models.TextField('Product description', blank=False, null=False)
    measure_unit = models.ForeignKey(MeasureUnit, on_delete=models.CASCADE, verbose_name='measure unit', null=True)
    category_product = models.ForeignKey(CategoryProduct, on_delete=models.CASCADE, verbose_name='Category Product', null=True)
    image = models.ImageField('Product image', upload_to='products/', blank=True, null=True)
    historical = HistoricalRecords()
    
    @property
    def _history_user(self):
        return self.changed_by
    
    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value

    class Meta:
        """Meta definition for Product."""

        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def __str__(self):
        """Unicode representation of Product."""
        return self.name


