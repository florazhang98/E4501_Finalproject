from django.db import models

class Squirrel(models.Model):
    Latitude=models.FloatField(blank=False)
    Longitude=models.FloatField(blank=False)
    Unique_Squirrel_ID=models.CharField(max_length=150, unique=True, blank=False)
    Shift=models.CharField(max_length=150, blank=True)
    Date=models.DateField(blank=True)
    Age=models.CharField(max_length=150, blank=True)
    Primary_Fur_Color=models.CharField(max_length=150, blank=True)
    Location=models.CharField(max_length=150, blank=True)
    Specific_Location=models.CharField(max_length=150, blank=True)
    Running=models.BooleanField(blank=True)
    Chasing=models.BooleanField(blank=True)
    Climbing=models.BooleanField(blank=True)
    Eating=models.BooleanField(blank=True)
    Foraging=models.BooleanField(blank=True)
    Other_Activities=models.BooleanField(max_length=100, blank=True)
    Kuks=models.BooleanField(blank=True)
    Quass=models.BooleanField(blank=True)
    Moans=models.BooleanField(blank=True)
    Tail_flags=models.BooleanField(blank=True)
    Tail_twitches=models.BooleanField(blank=True)
    Approaches=models.BooleanField(blank=True)
    Indifferent=models.BooleanField(blank=True)
    Runs_from=models.BooleanField(blank=True)
