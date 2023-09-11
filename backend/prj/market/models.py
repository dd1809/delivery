from django.db import models

from django.contrib.auth.models import User

class Provider(User):
    name = models.CharField(max_lenght=250, default='')
    phone = models.CharField(max_lenght=250, default='')
    rating = models.IntegerField(default=0)


