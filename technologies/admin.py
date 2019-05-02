from django.contrib import admin

from .models import Technology

class TechnologyAdmin(admin.ModelAdmin):
    list_display = ('software', 'softwaretype', 'endofsupport', 'disposition')
    list_filter = ('softwaretype', 'disposition')


admin.site.register(Technology, TechnologyAdmin)
