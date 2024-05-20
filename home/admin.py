from django.contrib import admin
from .models import Article, Messages, BlogsArticle

# Register your models here.
from django.contrib import admin
from .models import Article, Messages, BlogsArticle


class FilterByTitle(admin.SimpleListFilter):
    title = "کلید های پر تکرار"
    parameter_name = 'title'

    def lookups(self, request, model_admin):
        return (
            ('django', "DJANGO"),
            ('python', "PYTHON"),
        )

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(title__icontains=self.value())


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('author', 'title', 'description')
    search_fields = ('title',)
    list_filter = (FilterByTitle,)
    # You can create custom filter and use ready filter like status and every thing you want


admin.site.register(Messages)
admin.site.register(BlogsArticle)
