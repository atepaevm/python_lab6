from django.db import models

# Create your models here.

from django.db import models


class Item(models.Model):
    header = models.CharField(max_length=255)
    link = models.CharField(max_length=255)
    description = models.CharField(max_length=10000)
    #date = models.CharField(max_length=255)
    date = models.DateTimeField()

    @classmethod
    def create(cls, header, link, desc, date):
        item = cls(header=header, link=link, description=desc, date=date)
        return item

    class Meta:
        unique_together = ("header", "date")
