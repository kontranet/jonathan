from django.contrib import admin

from .models import Company
class CompaniesAdmin(admin.ModelAdmin):
    list_display = ('id', 'company_name', 'is_published', 'contact_person', 'phone', 'list_date')
    list_display_links = ('id', 'company_name')
    list_editable = ('is_published',)
    search_fields = ('company_name', 'contact_person', 'phone')
    list_per_page = 25

admin.site.register(Company, CompaniesAdmin)
