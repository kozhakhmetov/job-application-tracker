from django.db import models
import datetime
from datetime import datetime as dt


class Status(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return '{}: {}'.format(self.id, self.name)

    def to_json(self):
        return{
            'id': self.id,
            'name': self.name
        }


class Company(models.Model):   # CRUD
    name = models.CharField(max_length=200)

    def __str__(self):
        return '{}: {}'.format(self.id, self.name)

    def to_json(self):
        return{
            'id': self.id,
            'name': self.name
        }


class Position(models.Model):
    name = models.CharField(max_length=200)
    link = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    type = models.CharField(max_length=200)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    def __str__(self):
        return '{}: {}: {}: {}: {}'.format(self.name, self.link, self.location, self.type, self.company)

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'link': self.link,
            'location': self.location,
            'type': self.type
        }


class User(models.Model):
    login = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    lastName = models.CharField(max_length=200)
    firstName = models.CharField(max_length=200)
    leetcodeUrl = models.CharField(max_length=200)

    def __str__(self):
        return '{}: {}: {}: {}: {}'.format(self.login, self.password, self.lastName, self.firstName, self.leetcodeUrl)

    def to_json(self):
        return {
            'id': self.id,
            'login': self.login,
            'password': self.password,
            'lastName': self.lastName,
            'firstName': self.firstName,
            'leetcodeUrl': self.leetcodeUrl
        }




