from django.contrib import admin
from estimate_item.models import EstimateItemType, EstimateItemMaterial, EstimateItem


# Register your models here.
@admin.register(EstimateItemType)
class EstimateItemTypeAdmin(admin.ModelAdmin):
    list_display = [field.name for field in EstimateItemType._meta.fields]


@admin.register(EstimateItemMaterial)
class EstimateItemMaterialTypeAdmin(admin.ModelAdmin):
    list_display = [field.name for field in EstimateItemMaterial._meta.fields]


@admin.register(EstimateItem)
class EstimateItemAdmin(admin.ModelAdmin):
    list_display = [field.name for field in EstimateItem._meta.fields]
