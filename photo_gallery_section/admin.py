from django.contrib import admin
from photo_gallery_section.models import fixed_Photo
# Register your models here.

class photo_Gallery_Fixed_Image(admin.ModelAdmin):
    #  # Override the has_add_permission method to always return False
    # def has_add_permission(self, request):
    #     return False
    list_display=('name','image')
admin.site.register(fixed_Photo,photo_Gallery_Fixed_Image)