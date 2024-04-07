from django.db import models


class Phone(models.Model):
    name = models.CharField(u'Название', max_length=100)
    price = models.FloatField(u'Цена')
    image = models.CharField(u'Изображение', max_length=300)
    release_date = models.DateField(u'Дата выпуска')
    lte_exists = models.BooleanField(u'Наличие LTE', default=False)
    slug = models.SlugField(unique=True)

