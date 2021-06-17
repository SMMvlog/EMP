from django.contrib import admin
from .models import Emp

@admin.register(Emp)
class EmpAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'location','salary','DOJ']
