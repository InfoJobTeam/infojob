from django.urls import path
from .views import index, employer, employee

app_name = 'mainapp'

urlpatterns = [
    path('', index, name='index'),
    path('employer/', employer, name='employer'),
    path('employee/', employee, name='employee'),
]