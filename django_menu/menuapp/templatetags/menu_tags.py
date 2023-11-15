from django import template
from ..models import MenuItem

register = template.Library()


@register.simple_tag(takes_context=True)
def render_menu(context, menu_name, selected_menu_item=None):
    menu_items = selected_menu_item.children.all() if selected_menu_item \
        else MenuItem.objects.select_related('parent').filter(parent=None, menu_name=menu_name)
    current_path = context['request'].path
    return {'menu_items': menu_items, 'selected_menu_item': selected_menu_item, 'current_path': current_path}
