from django.contrib import admin
from footer_section.models import footer_logo,footer_paragraph,footer_number,footer_gmail,footer_location,developer,youtube_url
# Register your models here.

class test1(admin.ModelAdmin):
     # Override the has_add_permission method to always return False
    def has_add_permission(self, request):
        return False
    list_display=('name','footer_image')
admin.site.register(footer_logo,test1)


class test2(admin.ModelAdmin):
       # Override the has_add_permission method to always return False
    def has_add_permission(self, request):
        return False
    list_display=['footer_paragraph']
admin.site.register(footer_paragraph,test2)


class test3(admin.ModelAdmin):
       # Override the has_add_permission method to always return False
    def has_add_permission(self, request):
        return False
    list_display=['footer_number']
admin.site.register(footer_number,test3)

class test4(admin.ModelAdmin):
       # Override the has_add_permission method to always return False
    def has_add_permission(self, request):
        return False
    list_display=['footer_gmail']
admin.site.register(footer_gmail,test4)


class test5(admin.ModelAdmin):
       # Override the has_add_permission method to always return False
    def has_add_permission(self, request):
        return False
    list_display=['footer_location']
admin.site.register(footer_location,test5)


class test6(admin.ModelAdmin):
    list_display=('developer_name','developer_link')
admin.site.register(developer,test6)

class test7(admin.ModelAdmin):
    list_display=('name','url')
admin.site.register(youtube_url,test7)