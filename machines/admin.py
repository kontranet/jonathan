from django.contrib import admin

from .models import Machine
class MachinesAdmin(admin.ModelAdmin):
    list_display = ('id', 'machine_name', 'is_published', 'licence_no', 'operator_name', 'company', 'list_date')
    list_display_links = ('id', 'machine_name')
    list_filter = ('company',)
    list_editable = ('is_published',)
    search_fields = ('machine_name', 'licence_no', 'operator_name')
    list_per_page = 25
admin.site.register(Machine, MachinesAdmin)
