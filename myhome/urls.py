from django.urls import path

from .views import index,dadar,borivali,chembur



urlpatterns = [
    path('', index, name='home'),
    path('dadar', dadar, name='dadar'),
    path('borivali', borivali, name='borivali'),
    path('chembur', chembur, name='chembur'),
    

   
]