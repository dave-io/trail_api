from django.db import models
from core.models import BaseEntity

# Create your models here.
class Program(BaseEntity):
     name = models.TextField(default="")
     description = models.TextField(default="")
     image = models.TextField(default="")
     code = models.TextField(default="")

     class Meta:
            ordering = ['-created']



class Location(BaseEntity):
     name = models.TextField(default="")
     program = models.ForeignKey(Program, null=False, on_delete=models.CASCADE)


class Program_Sdg(BaseEntity):
    program = models.ForeignKey(Program, null=False, on_delete=models.CASCADE)
    sdgId = models.IntegerField("sdg_id")


class Program_Form(BaseEntity):
    program = models.ForeignKey(Program, null=False, on_delete=models.CASCADE)
    name = models.TextField(default="")
    link = models.TextField(default="")


class Program_Indicator(BaseEntity):
    programSdg = models.ForeignKey(Program_Sdg, null=False, on_delete=models.CASCADE)
    selectedIndicatorId = models.IntegerField("selected_indicator_id")


class Program_Indicator_Target(BaseEntity):
    Program_Indicator = models.ForeignKey(Program_Indicator, null=False, on_delete=models.CASCADE)
    Name = models.TextField(default="")
    Value = models.IntegerField(default=0)