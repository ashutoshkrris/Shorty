from django.contrib import admin
from .models import APIKey


# Register your models here.

@admin.register(APIKey)
class APIKeyAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'api_key', 'usage', 'expired', 'date_created')
    search_fields = ('email', 'api_key')
    ordering = ('-id',)
    list_filter = ('expired',)