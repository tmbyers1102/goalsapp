from django.conf import settings
from django.urls import include, path
from . import views
from .views import (
    CurrentGoalWeekUpdateView,
    home,
    CurrentGoalWeekDetailView,
    CurrentGoalWeekUpdateView,
)


app_name = "weeks"

urlpatterns = [
    path('', home, name='home'),
    path('weeks/<int:pk>/', CurrentGoalWeekDetailView.as_view(), name='week-detail'),
    path('weeks/<int:pk>/update/', CurrentGoalWeekUpdateView.as_view(), name='week-update'),
]