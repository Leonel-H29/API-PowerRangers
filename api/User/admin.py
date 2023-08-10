from django.contrib import admin
from .models import User
# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display=('username', 'email', 'is_superuser', 'is_staff' ,'is_active')
    search_fields=('username', 'email')
    ordering=['username']
    
admin.site.register(User, UserAdmin)