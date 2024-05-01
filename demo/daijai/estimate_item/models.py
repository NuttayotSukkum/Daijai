from django.db import models
from material.models import Material


# Create your models here.
class EstimateItemType(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name


class EstimateItem(models.Model):
    estimate_item_type = models.ForeignKey(
        EstimateItemType, on_delete=models.SET_NULL, null=True, blank=True
    )
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=9, decimal_places=2, null=True, blank=True)

    def __str__(self) -> str:
        return " - ".join([self.name, self.code])


class EstimateItemMaterial(models.Model):
    estimate_item = models.ForeignKey(EstimateItem, on_delete=models.CASCADE)
    material = models.ForeignKey(Material, on_delete=models.PROTECT)
    material_amount = models.IntegerField(default=1)
