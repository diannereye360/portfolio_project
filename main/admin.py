from django.contrib import admin
from .models import Project, ContactMessage


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['order', 'title', 'link', 'is_active']
    list_display_links = ['title']
    list_editable = ['order', 'is_active']
    ordering = ['order']


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ['received_at', 'name', 'email', 'subject', 'is_read']
    list_display_links = ['name']
    list_editable = ['is_read']
    list_filter = ['is_read']
    readonly_fields = ['name', 'email', 'subject', 'message', 'received_at']
    ordering = ['-received_at']
