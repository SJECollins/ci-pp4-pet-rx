from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Vet

# admin.site.register(Vet)


class AccountAdmin(UserAdmin):
    list_display = ('email', 'first_name', 'last_name', 'last_login', 'is_admin', 'is_active', 'is_staff')
    search_fields = ('email', 'first_name', 'last_name')
    readonly_fields = ('last_login', )

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()
    ordering = ('email', 'first_name', 'last_name', )


admin.site.register(Vet, AccountAdmin)
