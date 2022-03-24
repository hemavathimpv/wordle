from django.db import models

class WordleNames(models.Model):
    name = models.CharField(max_length=5)