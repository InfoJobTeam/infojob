from django.urls import path
from .views import *


app_name = 'employer'

urlpatterns = [
	path('', EmployerView.as_view(), name='employer'),
	# path('<int:pk>/', CvDetailView.as_view(), name='cv_detail'),
    # path('create/', CvCreate.as_view(), name='cv_create'),
    # path('update/<int:pk>/', CvUpdate.as_view(), name='cv_update'),
    # path('delete/<int:pk>/', CvDelete.as_view(), name='cv_delete'),
	]