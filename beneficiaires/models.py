# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Beneficaires(models.Model):
    idbeneficiaire = models.AutoField(db_column='idBeneficiaire', primary_key=True)  # Field name made lowercase.
    nom = models.CharField(db_column='Nom', max_length=50)  # Field name made lowercase.
    prenom = models.CharField(max_length=50)
    mail = models.CharField(max_length=50, blank=True, null=True)
    telephone = models.CharField(max_length=50, blank=True, null=True)
    adressepostale = models.CharField(db_column='adressePostale', max_length=50, blank=True, null=True)  # Field name made lowercase.
    motmairie = models.IntegerField(db_column='MotMairie')  # Field name made lowercase.
    cartedonnee = models.IntegerField(db_column='CarteDonnee')  # Field name made lowercase.
    remarque = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'beneficaires'


class Categories(models.Model):
    idcategorie = models.AutoField(db_column='idCategorie', primary_key=True)  # Field name made lowercase.
    nomCategorie = models.CharField(db_column='Nom', max_length=50)  # Field name made lowercase.
    image = models.CharField(db_column='Image', max_length=100, blank=True, null=True)  # Field name made lowercase.
    unite = models.CharField(db_column='Unite', max_length=10)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'categories'


class Nombrepart(models.Model):
    idbeneficiaire = models.OneToOneField(Beneficaires, models.DO_NOTHING, db_column='idBeneficiaire', primary_key=True)  # Field name made lowercase.
    number0_3 = models.IntegerField(db_column='0_3', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_4_14 = models.IntegerField(db_column='4_14', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_15_25 = models.IntegerField(db_column='15_25', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_26_64 = models.IntegerField(db_column='26_64', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_65plus = models.IntegerField(db_column='65plus', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.

    class Meta:
        managed = False
        db_table = 'nombrepart'


class Presencedistribution(models.Model):
    idbeneficiaire = models.OneToOneField(Beneficaires, models.DO_NOTHING, db_column='idbeneficiaire', primary_key=True)
    datedistribution = models.DateField(db_column='dateDistribution')  # Field name made lowercase.
    presence = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'presencedistribution'


class Produit(models.Model):
    idproduit = models.AutoField(db_column='idProduit', primary_key=True)  # Field name made lowercase.
    idcategorie = models.ForeignKey(Categories, models.DO_NOTHING, db_column='idCategorie')  # Field name made lowercase.
    nom = models.CharField(db_column='NomProduit', max_length=50)  # Field name made lowercase.
    quantite = models.IntegerField(db_column='Quantite')  # Field name made lowercase.
    seuilalerte = models.IntegerField(db_column='seuilAlerte')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'produit'

