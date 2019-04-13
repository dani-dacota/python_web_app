from django.db import models

# Create your models here.


class Person(models.Model):
    firstName = models.CharField(max_length=255)
    lastName = models.CharField(max_length=255)
    age = models.IntegerField()

    # added
    def __str__(self):
        return self.lastName + ', ' + self.firstName
