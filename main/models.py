from django.db import models

# Create your models here.
class Customer(models.Model):
    name = models.CharField('Name', max_length=50)
    surname = models.CharField('Surname', max_length=50)
    email = models.CharField('Email', max_length=50)
    password = models.CharField('Password', max_length=50)

    def __str__(self):
        return (f'Name: {self.name}, Surname: {self.surname}, '
         f'Email: {self.email}')