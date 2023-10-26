from django.contrib import admin

from Petstagram23.common.models import PhotoComment


# Register your models here.
@admin.register(PhotoComment)
class CommentAdmin(admin.ModelAdmin):
    ...