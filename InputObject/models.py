from django.db import models


class TimestampModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class InputObject(TimestampModel):
    name = models.CharField(max_length=255)
    code = models.FloatField()

    def __str__(self):
        return f'{self.name} : {self.code}'
