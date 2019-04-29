from ckeditor.widgets import CKEditorWidget
from django.contrib import admin
from .models import Post


# Register your models here.
admin.site.register(Post)
class PostAdmin(admin.ModelAdmin):
    fields = ('title', 'tags','short_desc', 'body','status')
    list_display = ('title', 'post_date','status')
    list_filter = ('post_date','status',)
    search_fields = ('title', 'body', 'short_desc')
    date_hierarchy = 'post_date'