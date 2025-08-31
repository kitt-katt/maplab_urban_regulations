from rest_framework import serializers
from .models import ParameterValue


class TepDataSerializer(serializers.ModelSerializer):
    """Сериализатор для вывода ТЭП."""
    # Получаем имя параметра из связанной модели Parameter
    parameter_name = serializers.CharField(source='parameter.name')
    # Получаем единицы измерения
    units = serializers.CharField(source='parameter.units', allow_null=True)

    class Meta:
        model = ParameterValue
        # Указываем, какие поля включать в JSON
        fields = ['parameter_name', 'value', 'units']