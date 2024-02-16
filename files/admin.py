from django.contrib import admin
from .models import *

class FileAdmin(admin.ModelAdmin):
    list_display = ['id', 'file', 'uploaded_at', 'processed']
    search_fields = ['id']
    list_filter = ['processed']
    
    class Meta:
        model = File

admin.site.register(File, FileAdmin)
