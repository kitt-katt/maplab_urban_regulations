from django.contrib import admin
from .models import Region, Parameter, ParameterValue


# Класс для встраивания значений на страницу редактирования Региона
class ParameterValueInline(admin.TabularInline):
    model = ParameterValue
    extra = 1  # Показывать одну пустую строку для добавления


# Регистрируем модель Региона и встраиваем в неё управление значениями
@admin.register(Region)
class RegionAdmin(admin.ModelAdmin):
    list_display = ('region_name', 'region_id')
    inlines = [ParameterValueInline]


# Регистрируем модель Параметра для отдельного управления
@admin.register(Parameter)
class ParameterAdmin(admin.ModelAdmin):
    list_display = ('name', 'units', 'description')
    search_fields = ('name', 'description') # Добавляем поиск для удобства