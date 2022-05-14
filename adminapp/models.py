from django.db import models


class Job(models.Model):
    name = models.CharField("Name", max_length=240)
    total_applied = models.IntegerField(default=0)
    publishedDate = models.DateField("Registration Date", auto_now_add=True)

    def __str__(self):
        return self.name