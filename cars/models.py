from django.db import models


class Car(models.Model):
    brand = models.CharField(max_length=100,help_text="Enter the brand of the car",verbose_name="Car Brand")
    country = models.CharField(max_length=100,help_text="Enter the country of the car",verbose_name="Car Country",default="Japan")
    year = models.IntegerField(help_text="Enter the year of the car",verbose_name="Manufacture Year")
    
    def __str__(self):
        return f'{self.brand} {self.year} {self.country}'