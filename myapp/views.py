from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib import messages
from .models import Meal
from .forms import MealForm

# Home page
def index(request):
    meals = Meal.objects.all()
    return render(request, 'myapp/index.html', {'meals': meals})

def about(request):
    return render(request, 'myapp/about.html')

# Read - List all meals
class MealListView(ListView):
    model = Meal
    template_name = 'myapp/meal_list.html'
    context_object_name = 'meals'
    paginate_by = 10

# Create - Add new meal
class MealCreateView(CreateView):
    model = Meal
    form_class = MealForm
    template_name = 'myapp/meal_form.html'
    success_url = reverse_lazy('meal_list')
    
    def form_valid(self, form):
        messages.success(self.request, 'Meal added successfully!')
        return super().form_valid(form)

# Read - View meal details
def meal_detail(request, pk):
    meal = get_object_or_404(Meal, pk=pk)
    return render(request, 'myapp/meal_detail.html', {'meal': meal})

# Update - Edit meal
class MealUpdateView(UpdateView):
    model = Meal
    form_class = MealForm
    template_name = 'myapp/meal_form.html'
    success_url = reverse_lazy('meal_list')
    
    def form_valid(self, form):
        messages.success(self.request, 'Meal updated successfully!')
        return super().form_valid(form)

# Delete - Remove meal
class MealDeleteView(DeleteView):
    model = Meal
    template_name = 'myapp/meal_confirm_delete.html'
    success_url = reverse_lazy('meal_list')
    
    def delete(self, request, *args, **kwargs):
        messages.success(request, 'Meal deleted successfully!')
        return super().delete(request, *args, **kwargs)

# Toggle meal completion status
def toggle_meal_status(request, pk):
    meal = get_object_or_404(Meal, pk=pk)
    meal.is_completed = not meal.is_completed
    meal.save()
    messages.success(request, f"Meal marked as {'completed' if meal.is_completed else 'pending'}!")
    return redirect('meal_list')
