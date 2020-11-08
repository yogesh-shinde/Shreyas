from django.contrib import admin
from .models import *
# Register your models here.


class CompanyAdmin(admin.ModelAdmin):
    list_display = ['company_id', 'company_name', 'is_indian']


class ModelAdmin(admin.ModelAdmin):
    list_display = ['model_id', 'model_name', 'company', 'internal_id']


admin.site.register(Mobile_Company, CompanyAdmin)
admin.site.register(Mobile_Model, ModelAdmin)
