from django.contrib import admin
from project.models import Project, ProjectEstimateItem
# Register your models here.

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Project._meta.fields]

@admin.register(ProjectEstimateItem)
class ProjectEstimateItemAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ProjectEstimateItem._meta.fields]

