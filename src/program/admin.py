from django.contrib import admin
from .models import Program

# Register your models here.
@admin.register(Program)
class ProgramAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'code', 'image', 'isDeleted', 'created', 'updated', 'createdBy', 'updatedBy')
    list_filter = ('name', 'created')
    list_per_page = 10
    search_fields = ['name']
    read_only_fields = ['created', 'updated']

