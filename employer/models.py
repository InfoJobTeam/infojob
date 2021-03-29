from django.db import models
from django.conf import settings
# from employee.models import CV


class Company(models.Model):

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='company')
    #dash = request.user.company.all()  для доступа ко всем компаниям пользователя
    company_name = models.CharField(max_length=150, verbose_name='Наименование')
    industry_name = models.CharField(max_length=150, verbose_name='индустрия')
    logo_pic = models.ImageField(upload_to='companies/%Y/%m/%d/', verbose_name='Логотип', default='companies/logo-placeholder.png')
    email = models.EmailField(max_length=150, unique=True)
    site_link = models.URLField(max_length=150, verbose_name='ссылка на сайт', blank=True)
    is_active = models.BooleanField(default=True, verbose_name='Активно')
    is_checked = models.BooleanField(default=True, verbose_name='Проверено')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Создано')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Обновлено')


class Vacancy(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='have_invitation' )
    position = models.CharField(max_length=150, verbose_name='должность')
    city = models.CharField(max_length=150, verbose_name='город')
    duties = models.TextField(verbose_name='обязанности')
    compensation = models.PositiveIntegerField(verbose_name='зарплата')
    is_active = models.BooleanField(default=True, verbose_name='активно')
    is_checked = models.BooleanField(default=True, verbose_name='проверено')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='создано')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='обновлено')


# class AddFavoriteCv(models.Model):
#     user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='have_favorite')
#     favorite_cv = models.ForeignKey(CV, on_delete=models.CASCADE, related_name='wish_cv')
#     # comments = models.TextField(verbose_name='коментарий')


# class Invitation(models.Model):
#     user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='have_invitation')
#     cv = models.ForeignKey(CV, on_delete=models.CASCADE, related_name='to_cv')
#     vacancy = models.ForeignKey(Vacancy, on_delete=models.CASCADE, related_name='my_vacancy')
#     comments = models.TextField(verbose_name='коментарий', blank=True)
#     created_at = models.DateTimeField(auto_now_add=True, verbose_name='создано')
#     updated_at = models.DateTimeField(auto_now=True, verbose_name='обновлено')