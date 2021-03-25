from django.urls import path
from .views import *


app_name = 'employee'

urlpatterns = [
	path('', EmployeeView.as_view(), name='employee'),
	path('<int:pk>/', CvDetailView.as_view(), name='cv_detail'),
    path('create/', CvCreate.as_view(), name='cv_create'),
    path('update/<int:pk>/', CvUpdate.as_view(), name='cv_update'),
    path('delete/<int:pk>/', CvDelete.as_view(), name='cv_delete'),
	]