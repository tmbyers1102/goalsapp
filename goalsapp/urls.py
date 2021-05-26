from django.contrib import admin
from django.urls import include, path
from goal_item.views import GoalItemCreateView, CurrentGoalWeekCreateView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('goals/create/', GoalItemCreateView.as_view(), name='goal-create'),
    path('weeks/create/', CurrentGoalWeekCreateView.as_view(), name='week-create'),
    path('', include('goal_item.urls', namespace='items')),
]
