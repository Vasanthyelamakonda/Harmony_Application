"""
URL configuration for BloodBank project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path

from Harmony import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',views.home,name='home'),
    path('register/',views.register,name='register'),
    path('adminlogin/',views.adminlogin,name='adminlogin'),
    path('userlogin/',views.userloign,name='userlogin'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    path('welcome/',views.welcome,name='welcome'),
    path('admindetails/',views.admindetails,name='admindetails'),
    path('adminsearch/',views.adminsearch,name='adminsearch'),
    path('userwelcome/',views.userwelcome,name='userwelcome'),
    path('usersearch/',views.usersearch,name='usersearch'),
    path('userupdate/',views.userupdate,name='userupdate'),
    path('logout/',views.logout,name='logout'),
    path('deleterecord/<int:user_id>',views.deleterecord,name='deleterecord'),
    path('updaterecord/<int:user_id>',views.updaterecord,name='updaterecord'),
    path('adminupdate/',views.update,name='adminupdate'),
]
