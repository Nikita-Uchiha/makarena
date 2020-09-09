from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from .managers import CustomUserManager
from django.utils.timezone import now
class CustomUser(AbstractUser):
    username = None
    phone = models.CharField(max_length=20, blank=True, null=True, unique = True)
    address_street = models.CharField(max_length=250, blank=True, null=True, default=None)
    address_house = models.CharField(max_length=250, blank=True, null=True, default=None)
    address_entrance = models.PositiveIntegerField(blank=True, null=True, default=None)
    address_apartment = models.PositiveIntegerField(blank=True, null=True, default=None)
    address_floor = models.PositiveIntegerField(blank=True, null=True, default=None)
    Birth_Date = models.DateField(blank=True, null=True)

    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = []
    objects = CustomUserManager()
    def __str__(self):
        return self.phone
