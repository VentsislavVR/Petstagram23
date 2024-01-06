from django.contrib import admin

from Petstagram23.common.models import PhotoComment,PhotoLike


# Register your models here.
@admin.register(PhotoComment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id','publication_date_and_time','photo')

@admin.register(PhotoLike)
class LikeAdmin(admin.ModelAdmin):
    ...