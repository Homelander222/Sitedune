from django.contrib import admin, messages

from .models import Dune, Category
from django.db.models.functions import Length


@admin.register(Dune)
class DuneAdmin(admin.ModelAdmin):
    list_display = ('title', 'time_create', 'is_published', 'cat', 'brief_info')
    list_display_links = ('title',)
    ordering = ('title',)
    list_editable = ('is_published', )
    list_per_page = 15
    actions = ('set_published', 'set_draft')

    @admin.display(description='Краткое описание', ordering=Length('content'))
    def brief_info(self, dune: Dune):
        return f"Описание {len(dune.content)} символов."

    @admin.action(description='Опубликовать выбранные записи')
    def set_published(self, request, queryset):
        count = queryset.update(is_published=Dune.Status.PUBLISHED)
        self.message_user(request, f'Изменено {count} записей')

    @admin.action(description='Снять с публикации выбранные записи')
    def set_draft(self, request, queryset):
        count = queryset.update(is_published=Dune.Status.DRAFT)
        self.message_user(request, f'{count} записей сняты с публикации!', messages.WARNING)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')