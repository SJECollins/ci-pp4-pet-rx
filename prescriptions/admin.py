from django.contrib import admin
from .models import Drug, Category

# Register your models here.


class DrugAdmin(admin.ModelAdmin):
    """
    Custom class for Drug display in admin panel.
    """
    list_display = ('name', 'dose', 'category', )
    list_filter = ('category', )
    search_fields = ('name', 'category', )


admin.site.register(Drug, DrugAdmin)
admin.site.register(Category)
