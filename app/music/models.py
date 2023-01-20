from django.db import models

# Create your models here.
class Artiste(models.Model):
    STYLE = [
        ("POP", "pop"),
        ("RAP", "rap"),
        ("CLASSIC", "classic"),
        ("ROCK", "rock"),
        ("UNDEFINED", "undefined"),
    ]
    nom = models.CharField(max_length=140)
    style = models.CharField(max_length=60, choices=STYLE)

    def __str__(self):
        return self.nom

class Chanson(models.Model):
    titre = models.CharField(max_length=140)
    durée = models.FloatField(max_length=140)
    date = models.DateTimeField()
    artiste = models.ForeignKey(Artiste, related_name="chansons", on_delete=models.CASCADE)

    def __str__(self):
        return self.titre