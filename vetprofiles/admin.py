from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Vet

# admin.site.register(Vet)


class AccountAdmin(UserAdmin):
    """
    Class for custom user model in admin panel.
    """
    list_display = (
        'email',
        'first_name',
        'last_name',
        'last_login',
        'is_admin',
        'is_active',
        )
    list_filter = ('is_active', )
    search_fields = ('email', 'first_name', 'last_name')
    readonly_fields = ('last_login', )

    filter_horizontal = ()
    fieldsets = ()
    add_fieldsets = (
        (None, {'fields': ('email', 'password1', 'password2', )}),
    )
    ordering = ('email', 'first_name', 'last_name', )


admin.site.register(Vet, AccountAdmin)
