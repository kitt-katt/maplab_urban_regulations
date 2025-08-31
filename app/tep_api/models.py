from django.db import models


class Region(models.Model):
    """Справочник регионов."""
    region_id = models.IntegerField(primary_key=True, verbose_name="Код региона")
    region_name = models.CharField(max_length=100, unique=True, verbose_name="Наименование региона")

    def __str__(self):
        return f"{self.region_name} ({self.region_id})"

    class Meta:
        verbose_name = "Регион"
        verbose_name_plural = "Регионы"


class Parameter(models.Model):
    """Справочник ТЭП параметров."""
    name = models.CharField(max_length=255, unique=True, verbose_name="Наименование параметра")
    description = models.TextField(blank=True, null=True, verbose_name="Описание")
    units = models.CharField(max_length=20, blank=True, null=True, verbose_name="Единицы измерения")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Параметр"
        verbose_name_plural = "Параметры"


class ParameterValue(models.Model):
    """Значения параметров для конкретных регионов."""
    region = models.ForeignKey(Region, on_delete=models.CASCADE, related_name="parameters", verbose_name="Регион")
    parameter = models.ForeignKey(Parameter, on_delete=models.CASCADE, related_name="values", verbose_name="Параметр")
    value = models.FloatField(verbose_name="Значение")

    def __str__(self):
        return f"{self.region.region_name}: {self.parameter.name} = {self.value}"

    class Meta:
        # Гарантируем, что для одного региона может быть только одно значение одного и того же параметра
        unique_together = ('region', 'parameter')
        verbose_name = "Значение параметра"
        verbose_name_plural = "Значения параметров"