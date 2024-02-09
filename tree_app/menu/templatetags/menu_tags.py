from django import template

from menu.models import Menu

register = template.Library()


@register.inclusion_tag('menu/draw_menu.html', name='draw_menu')
def get_menu(title):
    """Фильтрует меню по названию"""
    try:
        menu_items = Menu.objects.filter(menu_title=title, parent=None)
        return {'menu_items': menu_items, 'title': title}
    except Menu.DoesNotExist:
        return
