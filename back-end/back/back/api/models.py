from django.db import models
import datetime
from datetime import datetime as dt
from django.contrib.auth.models import User


# status of application might (Phone interview, Reject, Ghosted, Applied, )
# TODO: modify to multiple status such as {Applied and Phone interview}
# cannot be modified by user


class Status(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return '{}: {}'.format(self.id, self.name)


# company user
# every user has their own company list
# can be modified by user
# TODO: add created_by field

class Company(models.Model):   # CRUD
    name = models.CharField(max_length=200)

    def __str__(self):
        return '{}: {}'.format(self.id, self.name)


# each user creates position to apply
# TODO: add created_by field

class Position(models.Model):
    name = models.CharField(max_length=200)
    link = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    type = models.CharField(max_length=200)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    def __str__(self):
        return '{}: {}: {}: {}: {}'.format(self.name, self.link, self.location, self.type, self.company)


class CustomUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    login = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    lastName = models.CharField(max_length=200)
    firstName = models.CharField(max_length=200)
    leetcode_url = models.CharField(max_length=200)

    def __str__(self):
        return '{}: {}: {}: {}: {}'.format(self.login, self.password, self.lastName, self.firstName, self.leetcodeUrl)




