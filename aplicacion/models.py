# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models


class Codigo(models.Model):
    idcodigo = models.AutoField(primary_key=True)
    id_usuario = models.ForeignKey(User)
    enlace = models.CharField(max_length=500)
    codigodes = models.CharField(max_length=1000)

    def __str__(self):
        return '%s' % (self.id_usuario.username)
    class Meta:
        managed = True
        db_table = 'codigo'



