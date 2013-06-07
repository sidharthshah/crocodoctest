from django.db import models
from djcroco.models import CrocoModel

class Example(CrocoModel):
    name = models.CharField(max_length=255)
    file = models.FileField(upload_to='examples/')
    thumbnail = models.ImageField(upload_to='examples/thumbnails/', blank=True,
        null=True, editable=False)

    def __unicode__(self):
        return self.name

