from django.urls import path
from .views import print_name, print_surname, print_age, print_name_surname, print_name_surname_age

urlpatterns = [
    path('name/', print_name),
    path('surname/', print_surname),
    path('age/', print_age),
    path('name/surname/', print_name_surname),
    path('name/surname/age/', print_name_surname_age),
]
