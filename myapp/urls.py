from django.urls import path
from . import views

urlpatterns = [
    # Home pages
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    
    # Meal CRUD operations
    path('meals/', views.MealListView.as_view(), name='meal_list'),
    path('meals/create/', views.MealCreateView.as_view(), name='meal_create'),
    path('meals/<int:pk>/', views.meal_detail, name='meal_detail'),
    path('meals/<int:pk>/edit/', views.MealUpdateView.as_view(), name='meal_edit'),
    path('meals/<int:pk>/delete/', views.MealDeleteView.as_view(), name='meal_delete'),
    path('meals/<int:pk>/toggle/', views.toggle_meal_status, name='meal_toggle'),
]
