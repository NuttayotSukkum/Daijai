from django.contrib import admin
from material.models import (
    Category3,
    Material,
    MaterialDetail,
    MaterialField,
    MaterialFieldDetail,
)
from django.db.models import QuerySet


# Register your models here.
@admin.register(Category3)
class Category3Admin(admin.ModelAdmin):
    list_display = [field.name for field in Category3._meta.fields]


@admin.register(Material)
class MaterialAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Material._meta.fields]

    def generate_code(self, request, queryset: QuerySet[Material]):
        # Perform your action here
        for material in queryset:
            material_details = (
                MaterialDetail.objects.filter(material__id=material.id)
                .select_related("material_field_detail")
                .order_by("code_digit_order")
            )
            item_count = 0
            code = material.category_3.code
            descriptios = []
            for digit in material_details:
                code += digit.material_field_detail.code
                descriptios.append(digit.material_field_detail.name)
                item_count += 1
            material.code = code
            material.description = " ".join(descriptios)
            material.save()
        self.message_user(request, f"{queryset} were updated.")

    generate_code.short_description = "Generate Code"

    actions = ["generate_code"]


@admin.register(MaterialDetail)
class MaterialDetailAdmin(admin.ModelAdmin):
    list_display = [field.name for field in MaterialDetail._meta.fields]


@admin.register(MaterialField)
class MaterialFieldAdmin(admin.ModelAdmin):
    list_display = [field.name for field in MaterialField._meta.fields]


@admin.register(MaterialFieldDetail)
class MaterialFieldDetailAdmin(admin.ModelAdmin):
    list_display = [field.name for field in MaterialFieldDetail._meta.fields]
