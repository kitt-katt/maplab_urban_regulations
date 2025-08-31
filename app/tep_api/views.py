from rest_framework import generics
from .models import ParameterValue
from .serializers import TepDataSerializer


class TepListByRegionView(generics.ListAPIView):
    """
    API эндпоинт для получения списка ТЭП по ID региона.
    /api/v1/teps/{region_id}/
    """
    serializer_class = TepDataSerializer

    def get_queryset(self):
        """
        Этот метод возвращает отфильтрованный список объектов.
        """
        # Получаем region_id из URL
        region_id = self.kwargs['region_id']
        # Фильтруем значения по region_id
        # select_related('parameter') - критически важная оптимизация!
        # Она делает JOIN на уровне SQL и избавляет нас от N+1 запросов к БД.
        return ParameterValue.objects.filter(region_id=region_id).select_related('parameter')