# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Tag(models.Model):
    nom=models.CharField(max_length=200,null=True)

    def __str__(self):
        return self.nom

class Produit(models.Model):
    nom=models.CharField(max_length=200,null=True)
    prix=models.FloatField(null=True)
    tag=models.ManyToManyField(Tag)

    def __str__(self):
        return self.nom
