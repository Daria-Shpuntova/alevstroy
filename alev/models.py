from django.db import models

class CallMe(models.Model):
    name = models.CharField(max_length=150, verbose_name='Имя')
    tel = models.CharField(max_length=12, verbose_name='Телефон')
    text = models.TextField(verbose_name='Текст', null=True)

    class Meta:
        verbose_name = 'Позвонить',
        verbose_name_plural = 'Позвонить'

    def __str__(self):
        return self.name

class Repair(models.Model):
    slug = models.SlugField()
    title = models.CharField(max_length=120)
    article = models.TextField(verbose_name='Текст')
    etap = models.TextField(verbose_name='Этапы работ')

    class Meta:
        verbose_name = 'Вид ремонта',
        verbose_name_plural = 'Виды ремонта'

    def __str__(self):
        return self.title

class Other(models.Model):
    slug = models.SlugField()
    titel = models.CharField(max_length=120, null=True)
    text = models.TextField(verbose_name='Текст', null=True)

    class Meta:
        verbose_name = 'Прочие услуги',
        verbose_name_plural = 'Прочие услуги'

    def __str__(self):
        return self.titel


class Objects(models.Model):
    name_object = models.CharField(max_length=120)
    address = models.CharField(max_length=250, null=True)

    class Meta:
        verbose_name = 'Объект',
        verbose_name_plural = 'Объекты'

    def __str__(self):
        return self.name_object

class Image(models.Model):
    img = models.ImageField(upload_to='object')
    name = models.ForeignKey(Objects, null=True, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Фото',
        verbose_name_plural = 'Фото'


