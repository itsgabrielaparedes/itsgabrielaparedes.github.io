from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager,PermissionsMixin,  Group, Permission
from django.utils import timezone
from django.utils.translation import gettext as _

# Create your models here.

class Producto(models.Model):
    marca = models.CharField(max_length=200)
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField()
    ingrediente = models.CharField(max_length=500)
    tipo_de_piel = models.CharField(max_length=200)
    problemas_piel = models.CharField(max_length=500)
    foto = models.ImageField(upload_to='productos/')
    
    def __str__(self):
        return self.marca + ' | ' + self.nombre +  ' | '  + self.tipo_de_piel

class CustomUserManager(BaseUserManager):
    def create_user(self, email, full_name, password=None, **extra_fields):
        if not email:
            raise ValueError('El correo electrónico es obligatorio.')
        email = self.normalize_email(email)
        user = self.model(email=email, full_name=full_name, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, full_name, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser debe tener is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser debe tener is_superuser=True.')

        return self.create_user(email, full_name, password, **extra_fields)

class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    full_name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['full_name']

    groups = models.ManyToManyField(
        Group,
        verbose_name=_('groups'),
        blank=True,
        help_text=_('Un usuario obtendrá todos los permisos'),
        related_name='customuser_set', 
        related_query_name='user',
    )

    user_permissions= models.ManyToManyField(
        Permission,
        verbose_name=_('user permissions'),
        blank=True,
        help_text=_('Especifica permisos para este usuario'),
        related_name='customeruser_set',
        related_query_name='user',
    )
      
    def __str__(self):
        return self.email