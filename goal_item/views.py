from django.shortcuts import render
from django.http import HttpResponse
from .models import GoalItem, Agent, CurrentGoalDay, CurrentGoalWeek
from django.views import generic
from django.urls import reverse
from .forms import GoalItemModelForm


def item_list(request):
    items = GoalItem.objects.all()
    toms_items = GoalItem.objects.filter(agent=1)
    agents = Agent.objects.all()
    agent_goals = GoalItem.objects.all()
    context = {
        "items": items,
        "toms_items": toms_items,
        "agents": agents,
        "agent_goals": agent_goals
    }
    return render(request, "goal_item/item_list.html", context)


def item_detail(request, pk):
    item = GoalItem.objects.get(id=pk)
    context = {
        "item": item
    }
    return render(request, "goal_item/item_detail.html", context)


def this_week(request, pk):
    this_week = CurrentGoalWeek.objects.get(id=pk)
    weeks_possible_points = CurrentGoalWeek.objects.get(id=pk).choose_goals.count() * 5
    weeks_goals = CurrentGoalWeek.objects.get(id=pk).choose_goals.order_by('name')
    # weeks_earned_points = 
    context = { 
        "this_week": this_week,
        "weeks_possible_points": weeks_possible_points,
        "weeks_goals": weeks_goals,
        # "weeks_earned_points": weeks_earned_points,
    }
    return render(request, "goal_item/this_week.html", context)


class GoalItemCreateView(generic.CreateView):
    template_name = "goal_item/goalitem_create.html"
    form_class = GoalItemModelForm

    def get_success_url(self):
        print(self.goalitem)
        return reverse("items:item-list")

    def form_valid(self, form):
        instance = form.save(commit=False)
        # instance.user = self.request.user
        instance.save()
        self.goalitem = instance
        return super(GoalItemCreateView, self).form_valid(form)


