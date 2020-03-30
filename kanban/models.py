from django.db import models
# Elementy które potem migrują do bazy danych
class Dane(models.Model):
    nazwa = models.CharField(max_length=30)
    status = models.IntegerField()
    def __str__(self):
        return self.nazwa