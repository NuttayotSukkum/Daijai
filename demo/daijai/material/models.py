from django.db import models


# Create your models here.
class Category3(models.Model):
    name = models.CharField(max_length=50)
    code = models.CharField(max_length=5)

    def __str__(self) -> str:
        return self.code


class MaterialField(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name


class MaterialFieldDetail(models.Model):
    material_field = models.ForeignKey(MaterialField, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    code = models.CharField(max_length=10)

    def __str__(self) -> str:
        return " - ".join([self.material_field.name, self.name, self.code])


class Material(models.Model):
    category_3 = models.ForeignKey(Category3, on_delete=models.SET_NULL, null=True)
    code = models.CharField(max_length=20, null=True, blank=True)
    description = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self) -> str:
        return self.code if self.code else "-"


class MaterialDetail(models.Model):
    material = models.ForeignKey(Category3, on_delete=models.CASCADE)
    material_field_detail = models.ForeignKey(
        MaterialFieldDetail, on_delete=models.CASCADE
    )
    code_digit_order = models.PositiveSmallIntegerField()
