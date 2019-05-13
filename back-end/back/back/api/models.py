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

class Company(models.Model):   # CRUD
    name = models.CharField(max_length=200)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, default=0)

    def __str__(self):
        return '{}: {}'.format(self.id, self.name)


# each user creates position to apply

class Position(models.Model):
    name = models.CharField(max_length=200)
    link = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    type = models.CharField(max_length=200)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, default=0)

    def __str__(self):
        return '{}: {}: {}: {}: {}'.format(self.name, self.link, self.location, self.type, self.company)


# addition info
class UserInfo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=0)
    leetcode_url = models.CharField(max_length=200)


class Manager(models.Manager):
    def for_user(self, user):
        return self.filter(created_by=user)


class UserApplication(models.Model):
    position = models.ForeignKey(Position, on_delete=models.CASCADE)
    status = models.ForeignKey(Status, on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.CharField(max_length=200)
    recruiter_contact = models.CharField(max_length=200)
    applied_at = models.DateTimeField(auto_now=False, editable=True)

    objects = Manager()


