from django import template
from ..models import TreeMenu
from ..utils import queries_counter

register = template.Library()


@queries_counter
@register.inclusion_tag('tree_menu.html', takes_context=True)
def draw_menu(context: dict, menu_name: str) -> dict:
    root_tree = TreeMenu.objects.select_related('parent').all()
    lst = []
    for root in root_tree:
        lst.append(root)
    context['lst'] = lst
    print(menu_name)
    return context


