from django.contrib import admin
from django.utils.html import format_html

from . models import Team
# Register your models here.

class TeamAdmin(admin.ModelAdmin):
    def thumbnail(self,object): #fun used to add photo in admin form
        return format_html('<img src="{}" width="40" style = "border-radius:50px"/>'.format(object.photo.url))
    thumbnail.short_description = 'photo' # instead of thumbnail name for photo column now photo name will shown

    list_display = ['id','thumbnail','firstname','lastname','created_date','designation'] #which fields will display
    list_display_links = ('id','thumbnail','firstname',) # firstname now also clickable
    search_fields = ('firstname','lastname','designation') # by which field we want to search data
    list_filter = ('designation',) # will create filter box and filter based on designation
admin.site.register(Team,TeamAdmin)
