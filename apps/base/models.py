from django.db import models
from django.db.models.base import Model, ModelBase

# Create your models here.

class BaseModel(models.Model):
    """Model definition for BaseModel."""

    id = models.AutoField(primary_key=True)
    state = models.BooleanField('State', default= True)
    created_date = models.DateField('created date', auto_now=False, auto_now_add=True)
    modified_date = models.DateField('Modified date', auto_now=True, auto_now_add=False)
    deleted_date = models.DateField('Deleted date', auto_now=True, auto_now_add=False)

    class Meta:
        """Meta definition for BaseModel."""
        abstract=True
        verbose_name = 'BaseModel'
        verbose_name_plural = 'BaseModels'
