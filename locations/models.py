from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import pre_save, post_save, post_delete, pre_delete
from django.dispatch import receiver


class Symbol(models.Model):
    image = models.ImageField()

    def __str__(self):
        return self.image.name


class Country(models.Model):
    class Meta:
        verbose_name_plural = 'Countries'

    name = models.CharField(max_length=100)
    description = models.TextField(null=True)
    population = models.IntegerField(default=0)
    flag = models.OneToOneField(Symbol, on_delete=models.CASCADE)
    cities_count = models.IntegerField(default=0)
    users = models.ManyToManyField(User)

    def __str__(self):
        return self.name


class City(models.Model):
    class Meta:
        verbose_name_plural = 'Cities'

    name = models.CharField(max_length=100)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    longitude = models.FloatField()
    latitude = models.FloatField()

    def __str__(self):
        return self.name


@receiver(pre_save, sender=City)
def info_pre_add_city(sender, instance, **kwargs):
    print(instance.name + ' is going to be add in the database')


@receiver(post_save, sender=City)
def increase_cities_count(sender, instance, **kwargs):
    instance.country.cities_count += 1
    instance.country.save()


@receiver(pre_delete, sender=City)
def decrease_cities_count(sender, instance, **kwargs):
    instance.country.cities_count -= 1
    instance.country.save()


@receiver(post_delete, sender=City)
def info_post_delete_city(sender, instance, **kwargs):
    print(instance.name + ' was deleted from the database')