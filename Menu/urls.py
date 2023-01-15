from django.urls import path
from .admin import tree_menu_admin_site
from .views import IndexView


urlpatterns = [
    path("", IndexView.as_view()),
    path("admin/", tree_menu_admin_site.urls),
]
