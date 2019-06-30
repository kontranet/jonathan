from django.contrib import admin

from .models import Person

class PersonsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'is_published', 'dateofbirth', 'company', 'list_date')
    list_display_links = ('id', 'name')
    list_filter = ('company',)
    list_editable = ('is_published',)
    search_fields = ('name',)
    list_per_page = 25

admin.site.register(Person, PersonsAdmin)
