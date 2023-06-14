from django.contrib import admin
from .models import Comment, Submission, Recipe, MembersRecipes
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Recipe)
class RecipeAdmin(SummernoteModelAdmin):

    list_display = ('title', 'slug', 'status', 'created_on')
    search_fields = ['title', 'ingredients']
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('status', 'created_on')
    summernote_fields = ('recipe',)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'created_on', 'approved')
    list_filter = ('approved', 'created_on')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)


@admin.register(Submission)
class SubmissionAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_on', 'published')
    list_filter = ('published', 'created_on')
    search_fields = ('name', 'email', 'body')
    actions = ['publish_recipes']

    def publish_recipes(modeladmin, request, queryset):
        queryset.update(published=True)

    publish_recipes.short_description = "Publish selected recipes"


@admin.register(MembersRecipes)
class MembersRecipesAdmin(SummernoteModelAdmin):
    list_display = ('title', 'author', 'created_on')
    list_filter = ('title', 'author', 'created_on')
    search_fields = ('title', 'author', 'created_on')
    actions = ['publish_recipes']
