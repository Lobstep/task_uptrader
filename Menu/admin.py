from django.contrib import admin
from .models import Menu
from .forms import MenuItemForm


class MenuAdminSite(admin.AdminSite):
    pass


tree_menu_admin_site = MenuAdminSite(name="Menu admin")


class MenuItemInline(admin.StackedInline):
    model = Menu
    form = MenuItemForm


@admin.register(Menu, site=tree_menu_admin_site)
class MenuAdmin(admin.ModelAdmin):
    list_display = ["title"]
    model = Menu
    form = MenuItemForm
    inlines = [MenuItemInline]