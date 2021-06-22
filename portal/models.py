from django.contrib.auth.base_user import AbstractBaseUser
from phone_iso3166.country import phone_country
import pycountry
import phonenumbers
from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
from geopy import Nominatim


class User(AbstractBaseUser):

    def __str__(self):
        return self.email


class UserSettings(models.Model):
    User = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.User


class Address(models.Model):
    Street_number = models.CharField(max_length=10, default='No 58B')
    Street_name = models.TextField(max_length=250, default='Morison Crescent')
    City = models.CharField(max_length=20, default='Ikeja')
    State = models.CharField(max_length=30, default='Lagos')
    Country = models.TextField(max_length=30, default='Nigeria')
    Postal_code = models.IntegerField(default='100001')
    Country_code = models.TextField(max_length=4, default='NG')
    Latitude = models.FloatField(max_length=50, default='1.000055555')
    Longitude = models.FloatField(max_length=50, default='2.59595959')
    Full_address = models.CharField(max_length=250, default='full address')

    def save(self, *args, **kwargs):
        str1 = " "
        mapping = {country.name: country.alpha_2 for country in pycountry.countries}
        self.Full_address = f"{self.Street_number}, {self.Street_name}, {self.City}, {self.State} {self.Country}"
        place = self.Street_name
        geolocator = Nominatim(user_agent="geoapiExercises").geocode(place)
        data = geolocator.raw['display_name'].split()

        self.Longitude = geolocator.raw['lon']
        self.Latitude = geolocator.raw['lat']
        self.Postal_code = int(data[-2].replace(',', ''))
        self.Country_code = mapping.get(self.Country)
        super(Address, self).save(*args, **kwargs)

    def __str__(self):
        return self.Full_address


# # format phone number: This function format a given number to Nigeria mobile number
# def format_phone_number(number):
#     if len(number) == 13:
#         if number.startswith('234'):
#             return number
#     elif len(number) == 11:
#         if number.startswith('0'):
#             return number.replace('0', '234', 1)
#     elif len(number) == 10:
#         return '234' + number
#     return None


class Company(models.Model):
    Name = models.CharField(max_length=150)
    Icon = models.ImageField
    Email = models.EmailField
    Number = models.CharField(max_length=20)
    Address = models.ForeignKey(Address, on_delete=models.DO_NOTHING)

    def save(self, *args, **kwargs):
        local = phonenumbers.parse(self.Number, self.Address.Country_code)
        self.number = phonenumbers.format_number(local, phonenumbers.PhoneNumberFormat.E164)
        super(Company, self).save(*args, **kwargs)

    def __str__(self):
        return self.Name


class Site(models.Model):
    Name = models.CharField(max_length=100)
    Company = models.ForeignKey(Company, on_delete=models.CASCADE)
    Address = models.ForeignKey(Address, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.Name


class SiteSettings(models.Model):
    Site = models.ForeignKey(Site, on_delete=models.CASCADE)

    def __str__(self):
        return self.Site


class Controller(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class ControllerSettings(models.Model):
    controller = models.ForeignKey(Controller, on_delete=models.CASCADE)

    def __str__(self):
        return self.controller
