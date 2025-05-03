from django.contrib import admin
from .models import *
from django.utils.html import mark_safe
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

class Context(admin.StackedInline):
    model = Context
    extra = 1

class Comment(admin.StackedInline):
    model = Comment
    extra=0

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title','image_tag','intro','author','read_time','views','comments','published','important','category','created_at')
    search_fields = ('title',)
    list_filter = ('author','published','important','category','tags')
    date_hierarchy = 'created_at'
    inlines = (Context,Comment)

    def image_tag(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" width="160" height="90" />')
        return "No Image"

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name','email','phone','subject','seen','created_at')
    search_fields = ('name','email','subject')
    list_filter = ('seen','email','phone','created_at')

@admin.register(Newsletter)
class NewsletterAdmin(admin.ModelAdmin):
    list_display = ('email',)
    search_fields = ('email',)


@admin.register(Moment)
class MomentAdmin(admin.ModelAdmin):
    list_display = ('title','photo_tag','author','created_at','published')
    search_fields = ('title',)
    list_filter = ('author','published')

    def photo_tag(self, obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width="160" height="90" />')
        return "No photo"