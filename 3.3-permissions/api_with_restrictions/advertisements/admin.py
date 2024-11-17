from django.contrib import admin
from .models import Advertisement

@admin.register(Advertisement)
class AdvertisementAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'creator', 'created_at')
    list_filter = ('status', 'created_at')
    search_fields = ('title', 'description')
    ordering = ('-created_at',)
