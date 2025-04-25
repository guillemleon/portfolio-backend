from django.contrib import admin
from cloudinary.uploader import destroy
from .models import Project

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'start_date', 'end_date')

    def save_model(self, request, obj, form, change):
        if change:
            old = Project.objects.get(pk=obj.pk)
            if old.image and 'image' in form.changed_data:
                try:
                    destroy(old.image.public_id)
                    print(f"Removed from Cloudinary: {old.image.public_id}")
                except Exception as e:
                    print(f"Error removing from Cloudinary: {e}")
            if old.image_card and 'image_card' in form.changed_data:
                try:
                    destroy(old.image_card.public_id)
                    print(f"Removed from Cloudinary: {old.image_card.public_id}")
                except Exception as e:
                    print(f"Error removing from Cloudinary: {e}")

        super().save_model(request, obj, form, change)
