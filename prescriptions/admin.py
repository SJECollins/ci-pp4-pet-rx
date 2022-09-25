from django.contrib import admin
from .models import Drug

# Register your models here.


class DrugAdmin(admin.ModelAdmin):
    list_display = ('name', 'dose', 'category', )
    list_filter = ('category', )
    search_fields = ('name', 'category', )


admin.site.register(Drug, DrugAdmin)
