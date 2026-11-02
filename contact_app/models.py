from django.db import models

class Customer(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=35)
    phone_number = models.CharField(max_length=20)
    district = models.CharField(max_length=25)
    street = models.CharField(max_length=25)
    house = models.IntegerField()
    apartment = models.IntegerField()

def __str__(self):
    return self.first_name[:30]
# Create your models here.

class NextPerson(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    # class Meta:
    #     verbose_name = "Моя модель"
    #     verbose_name_plural = "Мои модели"

    class Meta:
        ordering = ['last_name', 'first_name']
        #ordering - задает порядок сортировки объектов модели в запросах

    def __str__(self):
        return f'{self.first_name[:30]}{self.last_name[:30]}'

class Blog(models.Model):
    title = models.CharField(max_length=50)
    slug = models.CharField(max_length=50)
    content = models.TextField(max_length=1000)
    excerpt = models.TextField(max_length=200)
    image = models.ImageField()
    author = models.CharField(max_length=30)

    class Meta:
        verbose_name = "Посты"
        verbose_name_plural = "Блог про Казань"

    def __str__(self):
        return f'{self.author[:30]} {self.title[:30]}'
