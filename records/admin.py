from django.contrib import admin
from .models import Record

# Register your models here.


class RecordAdmin(admin.ModelAdmin):
    """
    Custom class for Record display in admin panel.
    """
    list_display = ('name', 'surname', 'date_of_birth', 'species', 'breed', )
    list_filter = ('species', )
    search_fields = ('name', 'surname', 'species', )


admin.site.register(Record, RecordAdmin)
