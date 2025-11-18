from django.contrib import admin
from .models import Meal

@admin.register(Meal)
class MealAdmin(admin.ModelAdmin):
    list_display = ('day', 'meal_name', 'is_completed', 'created_at')
    list_filter = ('day', 'is_completed', 'created_at')
    search_fields = ('meal_name', 'description')
    readonly_fields = ('created_at', 'updated_at')
    fieldsets = (
        ('Meal Information', {
            'fields': ('day', 'meal_name', 'description')
        }),
        ('Status', {
            'fields': ('is_completed',)
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
