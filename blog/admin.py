from blog.models import Post, Comment
from django.contrib import admin


### Admin

class PostAdmin(admin.ModelAdmin):
    search_fields = ["title", "body"]
    list_display = ["title", "created"]
    exclude = ['slug']

class CommentAdmin(admin.ModelAdmin):
    list_display = ["post", "author", "created"]

admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)


