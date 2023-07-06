from django.contrib import admin

from .forms import CustomAdminLoginForm
from .models import CustomUser, Category, Post, Comment, Like


admin.site.login_form = CustomAdminLoginForm




class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_at', 'updated_at']


class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'category', 'created_at', 'updated_at']
    search_fields = ['title',  'author__username', 'category__name']




class CommentAdmin(admin.ModelAdmin):
    list_display = ['post', 'user', 'content', 'created_at', 'updated_at']


class LikeAdmin(admin.ModelAdmin):
    list_display = ['post', 'user', 'created_at']


admin.site.register(CustomUser)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Like, LikeAdmin)

