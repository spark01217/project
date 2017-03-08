from django.db import models


class Neighborhood(models.Model):
    code = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=250)
    price = models.IntegerField()
    crime = models.IntegerField()
    school = models.IntegerField()
    income = models.IntegerField()
    cta = models.IntegerField()

    def __str__(self):
        return str(self.code) + ', ' + self.name
