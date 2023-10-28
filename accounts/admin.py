from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User
from .forms import UserChangeForm, UserCreationForm


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm
    
    list_display = ('email', 'mobile_phone', 'full_name', 'id')
    list_filter = ('is_staff', 'is_active', 'is_superuser', 'created_at', 'updated_at')
    search_fields = ('email', 'full_name', 'mobile_phone', 'id')
    filter_horizontal = ('groups', 'user_permissions')
    ordering = ('email', 'created_at',)
    readonly_fields = ('created_at', )
    
    fieldsets = [
        (None, {"fields": ["email", "password"]}),
        ("Personal info", {"fields": ("mobile_phone", 'full_name')}),
        ("Permissions", {"fields": ("is_staff", 'is_active', 'is_superuser', 'groups', 'user_permissions')}),
        ('impoertand_data', {'fields': (
            'created_at',
            'updated_at',
            'last_login',
        )})
    ]
    
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("email", "password1", "password2"),
            },
        ),
    )
    
    