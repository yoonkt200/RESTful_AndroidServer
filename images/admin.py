from django.contrib import admin
from images.models import Image


class ImageAdmin(admin.ModelAdmin):
    model = Image
    list_display = ('title', 'label', 'id', 'created', 'modified')


admin.site.register(Image, ImageAdmin)