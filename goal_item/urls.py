from django.conf import settings
from django.urls import include, path
from . import views
from .views import item_detail, item_list, this_week, home

app_name = "items"

urlpatterns = [
    path('', home, name='home'),
    path('<pk>/', item_detail, name='item-detail'),
    path('thisweek/<pk>/', this_week, name='this-week'),
]