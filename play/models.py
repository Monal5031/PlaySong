from django.db import models

# Create your models here.


class Audio(models.Model):
    link = models.CharField(max_length=100, null=False, blank=True)
    title = models.CharField(max_length=15, null=False, blank=True)

    def __str__(self):
        return str(self.title) + ': ' + str(self.link)

