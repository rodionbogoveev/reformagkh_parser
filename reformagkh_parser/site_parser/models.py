from django.db import models


class Source(models.Model):
    region = models.CharField(
        verbose_name='Регион',
        max_length=64,
    )
    city = models.CharField(
        verbose_name='Город',
        max_length=64,
    )
    street = models.CharField(
        verbose_name='Улица',
        max_length=64,
    )
    house = models.CharField(
        verbose_name='Дом',
        max_length=64,
    )

    def __str__(self):
        return f'{self.region}, {self.city}, {self.street}, {self.house}'

    class Meta:
        verbose_name = 'Источник'
        verbose_name_plural = 'Источники'


class Result(models.Model):
    source = models.ForeignKey(
        Source,
        verbose_name='Источник',
        on_delete=models.SET_NULL,
        null=True,

    )
    year = models.PositiveSmallIntegerField(
        verbose_name='Год ввода дома в эксплуатацию',
        blank=True,
    )
    floors = models.PositiveSmallIntegerField(
        verbose_name='Количество этажей',
        blank=True,
    )
    updating = models.DateField(
        verbose_name='Последнее актуализирование информации',
        blank=True,
    )
    series = models.CharField(
        verbose_name='Серия, тип постройки здания',
        max_length=64,
        blank=True,
    )
    type_of_building = models.CharField(
        verbose_name='Тип дома',
        max_length=64,
        blank=True,
    )
    emergency = models.CharField(
        verbose_name='Факт признания дома аварийным',
        max_length=64,
        blank=True,
    )
    cadastre = models.CharField(
        verbose_name='Кадастровый номер земельного участка',
        max_length=64,
        blank=True,
    )
    floor = models.CharField(
        verbose_name='Тип перекрытий',
        max_length=64,
        blank=True,
    )
    walls = models.CharField(
        verbose_name='Материал несущих стен',
        max_length=64,
        blank=True,
    )

    def __str__(self):
        return f'{self.year}, {self.floors}, {self.updating}, {self.series}'

    class Meta:
        verbose_name = 'Результат'
        verbose_name_plural = 'Результаты'
