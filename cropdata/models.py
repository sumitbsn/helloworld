from __future__ import unicode_literals
from django.db import models


# Create your models here.
class Cropdata(models.Model):
    state = models.CharField(db_column='State', max_length=20)  # Field name made lowercase.
    district = models.CharField(db_column='District', max_length=30)  # Field name made lowercase.
    year = models.IntegerField(db_column='Year')  # Field name made lowercase.
    season = models.CharField(db_column='Season', max_length=11)  # Field name made lowercase.
    crop = models.CharField(db_column='Crop', max_length=25)  # Field name made lowercase.
    production = models.IntegerField(db_column='Production')  # Field name made lowercase.
    productivity = models.DecimalField(db_column='Productivity', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'cropdata'

class Pressure(models.Model):
    district = models.CharField(db_column='District', max_length=25)  # Field name made lowercase.
    year = models.IntegerField(db_column='Year')  # Field name made lowercase.
    january = models.IntegerField(db_column='January')  # Field name made lowercase.
    february = models.IntegerField(db_column='February')  # Field name made lowercase.
    march = models.IntegerField(db_column='March')  # Field name made lowercase.
    april = models.IntegerField(db_column='April')  # Field name made lowercase.
    may = models.IntegerField(db_column='May')  # Field name made lowercase.
    june = models.IntegerField(db_column='June')  # Field name made lowercase.
    july = models.IntegerField(db_column='July')  # Field name made lowercase.
    august = models.IntegerField(db_column='August')  # Field name made lowercase.
    september = models.IntegerField(db_column='September')  # Field name made lowercase.
    october = models.IntegerField(db_column='October')  # Field name made lowercase.
    november = models.IntegerField(db_column='November')  # Field name made lowercase.
    december = models.IntegerField(db_column='December')  # Field name made lowercase.
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'pressure'


class Temperature(models.Model):
    district = models.CharField(db_column='District', max_length=25)  # Field name made lowercase.
    year = models.IntegerField(db_column='Year')  # Field name made lowercase.
    january = models.IntegerField(db_column='January')  # Field name made lowercase.
    february = models.IntegerField(db_column='February')  # Field name made lowercase.
    march = models.IntegerField(db_column='March')  # Field name made lowercase.
    april = models.IntegerField(db_column='April')  # Field name made lowercase.
    may = models.IntegerField(db_column='May')  # Field name made lowercase.
    june = models.IntegerField(db_column='June')  # Field name made lowercase.
    july = models.IntegerField(db_column='July')  # Field name made lowercase.
    august = models.IntegerField(db_column='August')  # Field name made lowercase.
    september = models.IntegerField(db_column='September')  # Field name made lowercase.
    october = models.IntegerField(db_column='October')  # Field name made lowercase.
    november = models.IntegerField(db_column='November')  # Field name made lowercase.
    december = models.IntegerField(db_column='December')  # Field name made lowercase.
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'temperature'



