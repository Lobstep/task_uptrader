from django import template
from django.shortcuts import get_object_or_404
from ..models import Menu
from django.core.exceptions import ObjectDoesNotExist


register = template.Library()


@register.inclusion_tag('tree.html', takes_context=True)
def draw_menu(context, menu_name):
    menu = Menu.objects.filter(parent=None)
    local_context = {'menu_name': menu}
    requested_url = context['request'].path
    try:
        active_menu_item = Menu.objects.get(explicit_url=requested_url)
    except ObjectDoesNotExist:
        pass
    else:
        unwrapped_menu_item_ids = active_menu_item.get_elder_ids() + [active_menu_item.id]
        local_context['unwrapped_menu_item_ids'] = unwrapped_menu_item_ids
    return local_context


@register.inclusion_tag('tree.html', takes_context=True)
def draw_menu_item_children(context, menu_item_id):
    menu_name = Menu.objects.filter(pk=menu_item_id)
    local_context = {'menu_name': menu_name}
    if 'unwrapped_menu_item_ids' in context:
        local_context['unwrapped_menu_item_ids'] = context['unwrapped_menu_item_ids']
    return local_context