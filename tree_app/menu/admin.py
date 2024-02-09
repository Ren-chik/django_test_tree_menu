from django.contrib import admin

from menu.models import Menu


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    fields = ['menu_title', 'name_item', 'slug', 'parent']
