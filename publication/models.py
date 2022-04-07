from django.db import models
class Publication(models.Model):
    author = models.CharField(max_length=250)
    name = models.CharField(max_length=250)
    description = models.CharField(max_length=250)
    content1 = models.TextField(max_length=1000)
    content2 = models.TextField(max_length=1000)
    content3 = models.TextField(max_length=1000)
    def __str__(self) :
        return "%s (%i)" % (self.name, self.id)