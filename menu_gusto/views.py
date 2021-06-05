from django.http import HttpResponseRedirect, HttpResponseNotFound, HttpResponse
from django.shortcuts import render, redirect
from main_gusto.models import Dish, Category
from menu_gusto.forms import CategoryForm, DishForm
from django.forms import ModelChoiceField


# Create your views here.
def dish_info(request, pk):
    dish = Dish.objects.get(pk=pk)
    return render(request, 'dish.html', context={
        'dish': dish
    })


def dishes(request):
    categories = Category.objects.all().order_by('category_order')
    for item in categories:
        item.dishes = Dish.objects.filter(category=item.pk)
    return render(request, 'dishes.html', {'categories': categories})


def create_dish(request):
    if request.method == 'POST':
        form = DishForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/menu/dishes')

    form = DishForm
    return render(request, 'crerate_dish.html', context={'form': form})


def edit_dish(request, pk):
    categorys = Category.objects.all()
    try:
        dish = Dish.objects.get(id=pk)
        if request.method == "POST":
                dish.title = request.POST.get("title")
                dish_category= Category.objects.get(id=request.POST.get("category"))
                dish.category = dish_category
                if request.POST.get("is_visible")=='on':
                    dish.is_visible = True
                else:
                    dish.is_visible = False
                dish.photo = request.FILES.get('photo')
                dish.price = request.POST.get("price")
                dish.description = request.POST.get("description")
                dish.save()
                return HttpResponseRedirect("/menu/dishes")
        else:
            return render(request, "edit_dish.html", {"dish": dish, 'categories': categorys})
    except Category.DoesNotExist:
        return HttpResponseNotFound("<h2>Такої страви не існує</h2>")


def create_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    form = CategoryForm
    return render(request, 'create_category.html', context={'form': form})


def categories(request):
    categories = Category.objects.all()
    return render(request, 'categories.html', {'categories': categories})


def edit_category(request, pk):
    try:
        category = Category.objects.get(id=pk)

        if request.method == "POST":
            category.title = request.POST.get("title")
            category.category_order = request.POST.get("category_order")
            if request.POST.get("is_visible")=='on':
                category.is_visible = True
            else: category.is_visible = False
            if request.POST.get("is_special") == 'on':
                category.is_special = True
            else:
                category.is_special = False
            category.save()
            return HttpResponseRedirect("/menu/categories")
        else:
            return render(request, "edit_category.html", {"category": category})
    except Category.DoesNotExist:
        return HttpResponseNotFound("<h2>Такої категорії не існує</h2>")


def delete_category(request, pk):
    try:
        category = Category.objects.get(id=pk)
        if request.method == "POST":
            category.delete()
            return HttpResponseRedirect("/menu/categories")
        else:
            return render(request, "delete.html", {"name": " категорію " + category.title, "href": "/menu/categories"})
    except Category.DoesNotExist:
        return HttpResponseNotFound("<h2>Такої категорії не існує</h2>")


def delete_dish(request, pk):
    try:
        dish = Dish.objects.get(id=pk)
        if request.method == "POST":
            dish.delete()
            return HttpResponseRedirect("/menu/dishes")
        else:
            return render(request, "delete.html", {"name": ' блюдо ' + dish.title, "href": "/menu/dishes"})
    except Category.DoesNotExist:
        return HttpResponseNotFound("<h2>Такого блюда не існує</h2>")
