#-*- encoding:utf-8 -*-
from django.db import models
from django.utils import timezone
from model_utils.managers import InheritanceManager
from django.contrib.auth.models import (AbstractBaseUser,
                                        PermissionsMixin,
                                        BaseUserManager as DjBaseUserManager
                                        )


class BaseUserManager(DjBaseUserManager, InheritanceManager):
    """
    Manager for all Users types
    create_user() and create_superuser() must be overriden as we do not use
    unique username but unique email.
    """

    def create_user(self, email=None, password=None, **extra_fields):
        now = timezone.now()
        email = BaseUserManager.normalize_email(email)
        u = Usuario(email=email, is_superuser=False, last_login=now,
                        **extra_fields)
        u.set_password(password)
        u.save(using=self._db)
        return u

    def create_superuser(self, email, password, **extra_fields):
        u = self.create_user(email, password, **extra_fields)
        u.is_superuser = True
        u.is_active = True
        u.is_staff = True
        u.save(using=self._db)
        return u


# Create your models here.
class Usuario(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True, verbose_name=u'Correo electrónico')
    first_name = models.CharField(max_length=45, verbose_name=u'Nombre')
    last_name = models.CharField(max_length=45, verbose_name=u'Apellido Paterno')
    date_joined = models.DateTimeField(auto_now_add=True, editable=False)

    deck = models.ManyToManyField("Carta", related_name="cartas_usuario")

    is_superuser = False
    objects = BaseUserManager()

    USERNAME_FIELD = 'email'

    def __unicode__(self):
        return self.email

    def get_full_name(self):
        return self.first_name + ' ' + self.last_name

    def get_short_name(self):
        return self.first_name

    def get_username(self):
        return self.email
    

class Punto(models.Model):
    latitud=models.FloatField()
    longitud=models.FloatField()
    activo = models.BooleanField(default=True)

    def get_latitud(self):
        return self.latitud

    def get_longitud(self):
        return self.longitud

    def is_active(self):
        return self.activo
    
    
class Carta(models.Model):
    nombre=models.CharField(max_length=30)
    ataque=models.IntegerField()
    defensa=models.IntegerField()
    imagen=models.ImageField(blank=True,null=True)
    localizacion = models.ForeignKey(Punto)
