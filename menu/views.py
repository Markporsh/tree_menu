from django.shortcuts import render
from .utils import queries_counter


@queries_counter
def menu(request, slug=None):
    return render(request, 'menu.html', context={slug: slug})
