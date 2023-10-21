# Create your models here.

from django.db import models

class Task(models.Model):
        task = models.CharField(blank=False, max_length=250)
        is_comp = models.BooleanField(default=False)
        created_ts = models.DateTimeField(auto_now_add=True)
        updated_ts = models.DateTimeField(auto_now=True)

        def __str__(self):
                return self.task
