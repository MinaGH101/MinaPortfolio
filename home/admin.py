from django.contrib import admin
from .models import Projects, Messages

@admin.register(Projects)
class PojectsAdmin(admin.ModelAdmin):        
    list_display = ('id', 'title')

admin.site.register(Messages)