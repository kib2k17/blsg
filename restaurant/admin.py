from django.contrib import admin

from .models import ContactInquiry, GalleryPhoto, MenuItem, SiteSettings


@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return not SiteSettings.objects.exists()

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ("name", "category", "price", "is_available", "is_featured", "created_at")
    list_filter = ("category", "is_available", "is_featured")
    search_fields = ("name", "description")
    list_editable = ("is_available", "is_featured")


@admin.register(GalleryPhoto)
class GalleryPhotoAdmin(admin.ModelAdmin):
    list_display = ("id", "caption", "order")
    list_editable = ("caption", "order")


@admin.register(ContactInquiry)
class ContactInquiryAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "submitted_at", "is_read")
    list_filter = ("is_read", "submitted_at")
    list_editable = ("is_read",)
    search_fields = ("name", "email", "message")
    readonly_fields = ("submitted_at",)
