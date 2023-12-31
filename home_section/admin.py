from django.contrib import admin
from home_section.models import header_number, facebook_link, instagram_link, youtube_link, header_heading, header_paragraph, header_logo

# Register your models here.

class HeaderNumber(admin.ModelAdmin):
     # Override the has_add_permission method to always return False
    def has_add_permission(self, request):
        return False
    list_display = ['header_number']

admin.site.register(header_number, HeaderNumber)

class FacebookLink(admin.ModelAdmin):
     # Override the has_add_permission method to always return False
    def has_add_permission(self, request):
        return False
    list_display = ['facebook_link']

admin.site.register(facebook_link, FacebookLink)


class InstagramLink(admin.ModelAdmin):
     # Override the has_add_permission method to always return False
    def has_add_permission(self, request):
        return False
    list_display=['instagram_link']
admin.site.register(instagram_link,InstagramLink)

class YoutubeLink(admin.ModelAdmin):
     # Override the has_add_permission method to always return False
    def has_add_permission(self, request):
        return False
    list_display=['youtube_link']
admin.site.register(youtube_link,YoutubeLink)

class HeaderHeading(admin.ModelAdmin):
     # Override the has_add_permission method to always return False
    def has_add_permission(self, request):
        return False
    list_display=['header_heading']
admin.site.register(header_heading,HeaderHeading)

class HeaderParagraph(admin.ModelAdmin):
     # Override the has_add_permission method to always return False
    def has_add_permission(self, request):
        return False
    list_display=['header_paragraph']
admin.site.register(header_paragraph,HeaderParagraph)

class HeaderLogo(admin.ModelAdmin):
     # Override the has_add_permission method to always return False
    def has_add_permission(self, request):
        return False
    list_display=('name','header_logo')
admin.site.register(header_logo,HeaderLogo)



