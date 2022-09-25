from django.contrib import admin
from .models import Drugs

# Register your models here.


class DrugsAdmin(admin.ModelAdmin):
    list_display = ('name', 'dose', 'category', )
    list_filter = ('category', )
    search_fields = ('name', 'category', )


admin.site.register(Drugs, DrugsAdmin)
