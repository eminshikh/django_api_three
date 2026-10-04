from django.db import models

class ThreeNews (models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.URLField()

    def __str__(self):
        return self.title

      