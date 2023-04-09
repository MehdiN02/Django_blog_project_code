from django.contrib import admin

from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'datetime_modified', 'author')
    ordering = ('status', )
    # ordering = ('-status', ) # be sorat bar aks sort mikone

# admin.site.register(Post, PostAdmin)
