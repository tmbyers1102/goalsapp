from django.db.models import query
from goaldays.models import GoalDayOne
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from .models import GoalItem, Agent, CurrentGoalDay, CurrentGoalWeek
from django.views import generic
from django.views.generic import (
    DetailView,
    ListView,
    CreateView,
    UpdateView,
    DeleteView
)
from django.urls import reverse
from .forms import (
    GoalItemModelForm,
    CurrentGoalWeekModelForm,
    CurrentGoalWeekUpdateForm,
)


def home(request):
    context = {
        'weeks': CurrentGoalWeek.objects.filter(is_active_week=False),
        'd1_bool_yes': CurrentGoalWeek.objects.filter(day1_is_complete=True).count(),
        'd2_bool_yes': CurrentGoalWeek.objects.filter(day2_is_complete=True).count(),
        'active_week': CurrentGoalWeek.objects.filter(is_active_week=True)
    }
    return render(request, 'goal_item/home.html', context)


class CurrentGoalWeekDetailView(DetailView):
    model = CurrentGoalWeek
    # Dont think context_ob_name is needed anymore
    context_object_name = "week"

    def get_context_data(self, **kwargs):
        context = super(CurrentGoalWeekDetailView, self).get_context_data(**kwargs)
        week = self.get_object()
    # day 1
        if week.gd1_run:
            gd1_run_value = str("x")
        else:
            gd1_run_value = str("")
        if week.gd1_water:
            gd1_water_value = str("x")
        else:
            gd1_water_value = str("")
        if week.gd1_smoothie:
            gd1_smoothie_value = str("x")
        else:
            gd1_smoothie_value = str("")
        if week.gd1_read:
            gd1_read_value = str("x")
        else:
            gd1_read_value = str("")
        day_1_list = [week.gd1_run, week.gd1_water, week.gd1_smoothie, week.gd1_read]
        day_1_list_total = 0
        for x in day_1_list:
            if x == True:
                day_1_list_total += 1
        if day_1_list_total == 4:
            gd1_extra_point_value = str(":-)")
        else:
            gd1_extra_point_value = str(":-(")
    
    # day 2
        if week.gd2_run:
            gd2_run_value = str("x")
        else:
            gd2_run_value = str("")
        if week.gd2_water:
            gd2_water_value = str("x")
        else:
            gd2_water_value = str("")
        if week.gd2_smoothie:
            gd2_smoothie_value = str("x")
        else:
            gd2_smoothie_value = str("")
        if week.gd2_read:
            gd2_read_value = str("x")
        else:
            gd2_read_value = str("")
        day_2_list = [week.gd2_run, week.gd2_water, week.gd2_smoothie, week.gd2_read]
        day_2_list_total = 0
        for x in day_2_list:
            if x == True:
                day_2_list_total += 1
        if day_2_list_total == 4:
            gd2_extra_point_value = str(":-)")
        else:
            gd2_extra_point_value = str(":-(")
    
    # day 3
        if week.gd3_run:
            gd3_run_value = str("x")
        else:
            gd3_run_value = str("")
        if week.gd3_water:
            gd3_water_value = str("x")
        else:
            gd3_water_value = str("")
        if week.gd3_smoothie:
            gd3_smoothie_value = str("x")
        else:
            gd3_smoothie_value = str("")
        if week.gd3_read:
            gd3_read_value = str("x")
        else:
            gd3_read_value = str("")
        day_3_list = [week.gd3_run, week.gd3_water, week.gd3_smoothie, week.gd3_read]
        day_3_list_total = 0
        for x in day_3_list:
            if x == True:
                day_3_list_total += 1
        if day_3_list_total == 4:
            gd3_extra_point_value = str(":-)")
        else:
            gd3_extra_point_value = str(":-(")
    
    # day 4
        if week.gd4_run:
            gd4_run_value = str("x")
        else:
            gd4_run_value = str("")
        if week.gd4_water:
            gd4_water_value = str("x")
        else:
            gd4_water_value = str("")
        if week.gd4_smoothie:
            gd4_smoothie_value = str("x")
        else:
            gd4_smoothie_value = str("")
        if week.gd4_read:
            gd4_read_value = str("x")
        else:
            gd4_read_value = str("")
        day_4_list = [week.gd4_run, week.gd4_water, week.gd4_smoothie, week.gd4_read]
        day_4_list_total = 0
        for x in day_4_list:
            if x == True:
                day_4_list_total += 1
        if day_4_list_total == 4:
            gd4_extra_point_value = str(":-)")
        else:
            gd4_extra_point_value = str(":-(")
    
    # day 5
        if week.gd5_run:
            gd5_run_value = str("x")
        else:
            gd5_run_value = str("")
        if week.gd5_water:
            gd5_water_value = str("x")
        else:
            gd5_water_value = str("")
        if week.gd5_smoothie:
            gd5_smoothie_value = str("x")
        else:
            gd5_smoothie_value = str("")
        if week.gd5_read:
            gd5_read_value = str("x")
        else:
            gd5_read_value = str("")
        day_5_list = [week.gd5_run, week.gd5_water, week.gd5_smoothie, week.gd5_read]
        day_5_list_total = 0
        for x in day_5_list:
            if x == True:
                day_5_list_total += 1
        if day_5_list_total == 4:
            gd5_extra_point_value = str(":-)")
        else:
            gd5_extra_point_value = str(":-(")

    # context
        context = {
            'week': week,
            # day 1
            'gd1_run_value': gd1_run_value,
            'gd1_water_value': gd1_water_value,
            'gd1_smoothie_value': gd1_smoothie_value,
            'gd1_read_value': gd1_read_value,
            'gd1_extra_point_value': gd1_extra_point_value,
            'day_1_list_total': day_1_list_total,
            # day 2
            'gd2_run_value': gd2_run_value,
            'gd2_water_value': gd2_water_value,
            'gd2_smoothie_value': gd2_smoothie_value,
            'gd2_read_value': gd2_read_value,
            'gd2_extra_point_value': gd2_extra_point_value,
            'day_2_list_total': day_2_list_total,
            # day 3
            'gd3_run_value': gd3_run_value,
            'gd3_water_value': gd3_water_value,
            'gd3_smoothie_value': gd3_smoothie_value,
            'gd3_read_value': gd3_read_value,
            'gd3_extra_point_value': gd3_extra_point_value,
            'day_3_list_total': day_3_list_total,
            # day 4
            'gd4_run_value': gd4_run_value,
            'gd4_water_value': gd4_water_value,
            'gd4_smoothie_value': gd4_smoothie_value,
            'gd4_read_value': gd4_read_value,
            'gd4_extra_point_value': gd4_extra_point_value,
            'day_4_list_total': day_4_list_total,
            # day 5
            'gd5_run_value': gd5_run_value,
            'gd5_water_value': gd5_water_value,
            'gd5_smoothie_value': gd5_smoothie_value,
            'gd5_read_value': gd5_read_value,
            'gd5_extra_point_value': gd5_extra_point_value,
            'day_5_list_total': day_5_list_total,
        }
        return context


class CurrentGoalWeekCreateView(generic.CreateView):
    template_name = "goal_item/currentgoalweek_create.html"
    form_class = CurrentGoalWeekModelForm

    def get_success_url(self):
        print('!!VIEWS!!: week created')
        print(self.currentgoalweek)
        return reverse("weeks:week-detail", kwargs={
            "pk": self.currentgoalweek.id
        })

    def form_valid(self, form):
        instance = form.save(commit=False)
        # instance.user = self.request.user
        instance.save()
        self.currentgoalweek = instance
        return super(CurrentGoalWeekCreateView, self).form_valid(form)


class CurrentGoalWeekUpdateView(generic.UpdateView):
    template_name = "goal_item/currentgoalweek_update.html"
    model = CurrentGoalWeek
    form_class = CurrentGoalWeekUpdateForm

    def get_success_url(self):
        print('!!VIEWS!!: week updated')
        return reverse("weeks:home")

