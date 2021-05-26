from django.conf import settings
from django.urls import include, path
from . import views
from .views import home, CurrentGoalWeekDetailView

app_name = "weeks"

urlpatterns = [
    path('', home, name='home'),
    path('weeks/<int:pk>/', CurrentGoalWeekDetailView.as_view(), name='week-deatil'),
]