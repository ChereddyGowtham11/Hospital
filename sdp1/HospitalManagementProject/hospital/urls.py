"""
URL configuration for HospitalManagementProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from hospital.views import (home,base,contact,about,Login,Index,Logout_admin,View_Doctor, Delete_Doctor,
                            Add_Doctor,View_Patient,Delete_Patient,Add_Patient,View_Appointment,Add_Appointment,Delete_Appointment)
urlpatterns = [
        path('', home, name="home"),
        path('contact/', contact, name="contact"),
        path('about/', about, name="about"),
        path('admin_login/', Login, name="admin_login"),
        path('logout/', Logout_admin, name="logout_admin"),
        path('index/', Index, name="dashboard"),
        path('view_doctor/', View_Doctor, name="view_doctor"),
        path('add_doctor/', Add_Doctor, name="add_doctor"),
        path('view_patient/', View_Patient, name="view_patient"),
        path('view_appointment/', View_Appointment, name="view_appointment"),
        path('add_appointment/', Add_Appointment, name="add_appointment"),
        path('add_patient/', Add_Patient, name="add_patient"),
        path('delete_doctor(?p<int:pid>)/', Delete_Doctor, name="delete_doctor"),
        path('delete_patient(?p<int:pid>)/', Delete_Patient, name="delete_patient"),
        path('delete_Appointment(?p<int:pid>)/', Delete_Appointment, name="delete_appointment"),

]
