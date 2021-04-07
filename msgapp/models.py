from django.db import models
from django.conf import settings
from employee.models import CV
from employer.models import Vacancy




# class EmployerCvRelation(models.Model):
#     employer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='employers')
#     vacancy = models.ForeignKey(Vacancy, on_delete=models.CASCADE, related_name='vacancies')
#     in_bookmarks = models.BooleanField(default=False)
#
#     def __str__(self):
#         return f'{self.vacancy.position}, {self.vacancy.compensation}, {self.vacancy.company}'
#
#
# class EmployeeVacancyRelation(models.Model):
#     employee = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='staff')
#     cv = models.ForeignKey(CV, on_delete=models.CASCADE, related_name='cvs')
#     in_bookmarks = models.BooleanField(default=False)
#
#
#     def __str__(self):
#         return f'{self.cv.position_seek}, {self.cv.position_seek}, {self.cv.first_name}, {self.cv.first_name}'



class AddFavoriteVacancy(models.Model):
    employer = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='employers', verbose_name='Работодатели')
    vacancy = models.ForeignKey(Vacancy, on_delete=models.CASCADE, related_name='vacancies', verbose_name='Вакансии')
    in_bookmarks = models.BooleanField(default=False)


    def __str__(self):
        return f'{self.vacancy.position}, {self.vacancy.compensation}, {self.vacancy.company}'


    class Meta:
        verbose_name = 'Избранные вакансии'
        verbose_name_plural = 'Избранные вакансии'
        ordering = ['vacancy']



class AddFavoriteCv(models.Model):
    employee = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='staff')
    cvs = models.ForeignKey(CV, on_delete=models.CASCADE, related_name='resumes')
    in_bookmarks = models.BooleanField(default=False)


    def __str__(self):
        return f'{self.cvs.position_seek}, {self.cvs.position_seek}, {self.cvs.first_name}, {self.cvs.first_name}'

    class Meta:
        verbose_name = 'Избранные резюме'
        verbose_name_plural = 'Избранные резюме'
        ordering = ['cvs']



# class Invitation(models.Model):
#     user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='have_invitation')
#     cv = models.ForeignKey(CV, on_delete=models.CASCADE, related_name='to_cv')
#     vacancy = models.ForeignKey(Vacancy, on_delete=models.CASCADE, related_name='my_vacancy')
#     comments = models.TextField(verbose_name='коментарий', blank=True)
#     created_at = models.DateTimeField(auto_now_add=True, verbose_name='создано')
#     updated_at = models.DateTimeField(auto_now=True, verbose_name='обновлено')


# class Response(models.Model):
#     user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='have_response')
#     cv = models.ForeignKey(Vacancy, on_delete=models.CASCADE, related_name='my_cv')
#     vacancy = models.ForeignKey(Vacancy, on_delete=models.CASCADE, related_name='to_vacancy')
#     comments = models.TextField(verbose_name='коментарий', blank=True)
#     created_at = models.DateTimeField(auto_now_add=True, verbose_name='создано')
#     updated_at = models.DateTimeField(auto_now=True, verbose_name='обновлено')