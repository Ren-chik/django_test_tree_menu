from django.shortcuts import render
from django.views.generic import TemplateView


class MenuRender(TemplateView):
    template_name = 'menu/menu.html'


def show_child(request, slug):
    context = {
        'slug' : slug
    }
    return render(request, 'menu/child.html', context)
