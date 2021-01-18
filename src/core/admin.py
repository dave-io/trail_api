from django.contrib import admin

from core.models import Indicator, SDG

# Register your models here.
@admin.register(SDG)
class ProgramAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'image', 'isDeleted', 'created', 'updated', 'createdBy', 'updatedBy')
    list_filter = ('name', 'created')
    list_per_page = 10
    search_fields = ['name']
    read_only_fields = ['created', 'updated']


@admin.register(Indicator)
class IndicatorAdmin(admin.ModelAdmin):
    list_display = ('description', 'isDeleted', 'created', 'updated', 'createdBy', 'updatedBy')
    list_filter = ('description', 'created')
    list_per_page = 10
    search_fields = ['description']
    read_only_fields = ['created', 'updated']