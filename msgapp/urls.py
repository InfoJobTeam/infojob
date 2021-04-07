from django.urls import path
from .views  import *

app_name = 'msgapp'

urlpatterns = [
    path('', HomepageView.as_view(), name='index'),
    path('cv/<int:pk>/add', add_favorite_cv, name='add_favarite_cv'),
    path('cv/<int:pk>/remove', remove_favorite_cv, name='remove_favarite_cv'),
    path('cv/<int:pk>/remove', add_favorite_vacancy, name='add_favarite_vacancy'),
    path('cv/<int:pk>/remove', remove_favorite_vacancy, name='remove_favarite_vacancy'),
]