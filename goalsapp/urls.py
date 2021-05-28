from django.contrib import admin
from django.urls import include, path
from goal_item.views import CurrentGoalWeekCreateView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('weeks/create/', CurrentGoalWeekCreateView.as_view(), name='week-create'),
    path('', include('goal_item.urls', namespace='items')),
]
