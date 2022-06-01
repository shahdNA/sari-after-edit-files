from django.db import models


class Country(models.Model):
    name = models.CharField(null=True, blank=False, max_length=255, )
    code = models.CharField(null=True, max_length=150, )

    def __str__(self):
        return self.name


class City(models.Model):
    name = models.CharField(null=True, blank=False, max_length=255, )
    country = models.ForeignKey('Country', null=True, on_delete=models.CASCADE, related_name='cities', )

    def __str__(self):
        return self.name


class Restaurant(models.Model):
    name = models.CharField(null=True, blank=False, max_length=255, )
    owner_email = models.EmailField(null=True, blank=False, )
    city = models.ForeignKey('City', null=True, blank=False, max_length=255, on_delete=models.CASCADE,
                             related_name='restaurants', )
    address = models.TextField()

    def __str__(self):
        return self.name
