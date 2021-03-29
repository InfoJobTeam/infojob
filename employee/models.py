from django.db import models
from django.conf import settings


class CV(models.Model):
    M = 'MALE'
    F = 'FEMALE'
    SEX = [(M, 'Male'), (F, 'Female')]

    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='cv')
    # dash = request.created_by.cv.all()  для доступа ко всем резюме пользователя
    user_pic = models.ImageField(upload_to='users/%Y/%m/%d/', verbose_name='Фото', blank=True)
    position_seek = models.CharField(max_length=250, verbose_name='желаемая должность')
    compensation_seek = models.PositiveIntegerField(verbose_name='желаемая зарплата')
    first_name = models.CharField(max_length=150, verbose_name='имя')
    middle_name = models.CharField(max_length=150, verbose_name='отчество')
    family_name = models.CharField(max_length=150, verbose_name='фамилия')
    gender = models.CharField(max_length=10, choices=SEX, verbose_name='пол')
    birthday = models.DateField(verbose_name='день рождения')
    city = models.CharField(max_length=150, verbose_name='город')
    email = models.EmailField(max_length=150, unique=True)
    profession = models.CharField(max_length=150, verbose_name='профессия')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='создано')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='обновлено')

    def __str__(self):
        return f"{self.family_name} {self.first_name}, {self.position_seek}"

    class Meta:
        verbose_name = 'Резюме'
        verbose_name_plural = 'Резюме'
        ordering = ['-created_at', 'family_name']


class JobExp(models.Model):
    cv = models.ForeignKey(CV, on_delete=models.CASCADE, related_name="experiences")
    # object.experiences.all()
    employer = models.CharField(max_length=150, verbose_name='работодатель')
    position = models.CharField(max_length=150, verbose_name='должность')
    start_at = models.DateField(verbose_name='начало работы')
    finish_at = models.DateField(verbose_name='дата увольнения')

    class Meta:
        verbose_name = 'Опыт работы'
        ordering = ['-finish_at']



# class Education(models.Model):
#
#     BACHALOR = 'БАКАЛАВР'
#     MASTER = 'МАГИСТР'
#     DOCTOR = 'ДОКТОР'
#     SPECIALIST = 'СПЕЦИАЛИСТ'
#     GRADE = [(BACHALOR, 'Бакалавр'), (MASTER, 'Магистр'), (DOCTOR, 'Доктор'), (SPECIALIST, 'Специалист')]
#
#     cv = models.ForeignKey(CV, on_delete=models.CASCADE, related_name="educations")
#     # object.educations.all()
#     college_name = models.CharField(max_length=150, verbose_name='Учебное заведение')
#     specialization = models.CharField(max_length=150, verbose_name='специальность')
#     grade = models.CharField(max_length=150, choices=GRADE, verbose_name='степень')
#     graduated_at = models.DateField(verbose_name='окончание учебы')



# class AddFavoriteVacancy(models.Model):
#     user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='have_favorite')
#     favorite = models.ForeignKey(Vacancy, on_delete=models.CASCADE, related_name='wish_vacancy')
#     # comments = models.TextField(verbose_name='коментарий')
#     created_at = models.DateTimeField(auto_now_add=True, verbose_name='создано')


# class Response(models.Model):
#     user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='have_response')
#     cv = models.ForeignKey(Vacancy, on_delete=models.CASCADE, related_name='my_cv')
#     vacancy = models.ForeignKey(Vacancy, on_delete=models.CASCADE, related_name='to_vacancy')
#     comments = models.TextField(verbose_name='коментарий', blank=True)
#     created_at = models.DateTimeField(auto_now_add=True, verbose_name='создано')
#     updated_at = models.DateTimeField(auto_now=True, verbose_name='обновлено')