from django.db import models
from django.db.models.expressions import Value

# Create your models here.


class BaseEntity(models.Model):
    id = models.AutoField("id", primary_key=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    createdBy = models.IntegerField("created_by", default=0)
    updatedBy = models.IntegerField("updated_by", default=0)
    isDeleted = models.BooleanField("is_deleted", default=False)

    class Meta:
        abstract = True  # Set this model as Abstract


class SDG(BaseEntity):
    name = models.TextField(default="")
    description = models.TextField(default="")
    image = models.TextField(default="")

    class Meta:
        ordering = ['name']


class Indicator(BaseEntity):
    description = models.TextField(default="")
    sdg = models.ForeignKey(SDG, null=False, on_delete=models.CASCADE)


# class Sdg_Indicator(BaseEntity):
#     sdgIndicator = models.ForeignKey(SDG, null=False, on_delete=models.CASCADE)
#     selectedIndicatorId = models.IntegerField("selected_indicator_id")
