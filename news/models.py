from django.db import models


class News(models.Model):
    # Imagen para el calendario roster
    calendary_roster = models.ImageField(upload_to='images/')
    # Fichas descripción guild (contactos)
    rexx_summary = models.CharField(max_length=200)
    # Información de contacto y descripción (raza/skill tree)
    contact = models.CharField(max_length=20)
    ds_contact = models.CharField(max_length=20)
    # Recrutamiento descripción y cargos
    rec_summary = models.CharField(max_length=200)
