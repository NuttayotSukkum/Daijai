from django.db import models
from estimate_item.models import EstimateItem


# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=255)
    created = models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name


class ProjectEstimateItem(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    estimate_item = models.ForeignKey(
        EstimateItem, on_delete=models.PROTECT, null=True, blank=True
    )
    estimate_item_amount = models.IntegerField(default=1)
