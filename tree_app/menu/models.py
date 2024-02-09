from django.db import models


class Menu(models.Model):
    """Модель для меню, где menu_title - название меню"""
    menu_title = models.CharField(max_length=100, default='main_menu')
    name_item = models.CharField(max_length=100)
    slug = models.SlugField(max_length=150)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True, related_name='sub_menu')

    class Meta:
        verbose_name = 'Меню'
        verbose_name_plural = 'Меню'

    def __str__(self):
        return self.name_item
