from django.shortcuts import render, redirect
import datetime
from .models import Category, Dish, Events, Banners
from .forms import UserMessageForm

def test(request):
    return render(request,'test.html')

def main(request):
    if request.method == 'POST':
        form = UserMessageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')


    banners = Banners.objects.filter(is_visible=True)

    special_categories = Category.objects.filter(is_visible=True).filter(is_special=True).order_by('category_order')
    for item in special_categories:
        item.dishes = Dish.objects.filter(category=item.pk).filter(is_visible=True)

    categories = Category.objects.filter(is_visible=True).filter(is_special=False).order_by('category_order')
    for item in categories:
        item.dishes = Dish.objects.filter(category=item.pk).filter(is_visible=True)

    events = Events.objects.filter(event_date__gte = datetime.date.today())
    users_masseges_form = UserMessageForm
    return render(request, 'index.html', context={'categories':categories,
                                                  'special_categories' : special_categories,
                                                  'banners' : banners,
                                                  'events' : events,
                                                  'form':users_masseges_form})
