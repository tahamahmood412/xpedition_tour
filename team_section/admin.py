from django.contrib import admin
from team_section.models import team_members
# Register your models here.
class test3(admin.ModelAdmin):
    list_display=('name','title','image')
admin.site.register(team_members,test3)