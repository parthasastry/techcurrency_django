from django.db import models
from datetime import datetime

class Technology(models.Model):
    software = models.CharField(max_length=200)
    softwaretype = models.CharField(max_length=50)
    endofsupport = models.DateField(blank=True)
    disposition = models.CharField(max_length=20)
    def __str__(self):
        return self.software



