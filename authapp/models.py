from django.db import models
from django.contrib.auth.models import AbstractUser




class InfojobUser(AbstractUser):

    EMPLOYEE = 'EMPLOYEE'
    EMPLOYER = 'EMPLOYER'
    ROLE = [(EMPLOYEE, 'Employee'), (EMPLOYER, 'Employer')]

    avatar = models.ImageField(upload_to='users_avatars', verbose_name='аватар', blank=True)
    email = models.EmailField(max_length=50, unique=True)
    password = models.CharField(max_length=50, verbose_name='пароль')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='cоздано')
    user_role = models.CharField(choices=ROLE, default=EMPLOYEE, verbose_name='роль')

