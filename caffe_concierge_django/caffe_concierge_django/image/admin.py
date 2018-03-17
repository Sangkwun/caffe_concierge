from django.contrib import admin
from . import models

@admin.register(models.Image)
class ImageAdmin(admin.ModelAdmin):

    search_fields = (
        'name',
    )

    list_display = (
        'name',
    )