from django import forms
from main_gusto.models import Category, Dish


class DishForm(forms.ModelForm):
    title = forms.CharField(initial="dish", max_length=50)
    price = forms.IntegerField(widget=forms.NumberInput)
    is_visible = forms.CheckboxInput()
    description = forms.CharField(initial="description", max_length=50)
    category = forms.ModelChoiceField(queryset=Category.objects.all())
    photo = forms.ImageField()

    class Meta():
        model = Dish
        fields = ('title', 'price', 'is_visible', 'description', 'category', 'photo')


class CategoryForm(forms.ModelForm):
    title = forms.CharField(initial="category", max_length=50,
                            widget=forms.TextInput(attrs={'type': 'text', 'id': 'name', 'class': 'form-control',
                                                          'placeholder': 'Ім\'я', 'required': 'required'}))
    category_order = forms.IntegerField(widget=forms.NumberInput)
    is_visible = forms.CheckboxInput(attrs={'id': 'is_visible', 'checked': 'checked'})
    is_special = forms.CheckboxInput(attrs={'id': 'is_special', 'checked': 'checked'})

    class Meta():
        model = Category
        fields = ('title', 'category_order', 'is_visible', 'is_special')
