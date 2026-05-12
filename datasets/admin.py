from django.contrib import admin
from .models import Dataset, DatasetVersion, DatasetMetadata

class MetadataInline(admin.TabularInline):
    model = DatasetMetadata

class VersionInline(admin.TabularInline):
    model = DatasetVersion

@admin.register(Dataset)
class DatasetAdmin(admin.ModelAdmin):
    inlines = [MetadataInline, VersionInline]
    list_display = ('title', 'owner', 'status', 'visibility')
    list_filter = ('status', 'visibility', 'category')