"""
URL configuration for dairyApp project.

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
from diary.views import Home,getAllEntries,AddEntry,getIndividualEntry
from django.conf.urls import handler404
from diary.views import Error_404_view 

handler404 = Error_404_view

urlpatterns = [
    path('',Home),
    path('view-all-entries/',getAllEntries),
    path('add-new-entry/',AddEntry),
    path('diary/<int:id>/',getIndividualEntry),
    path('admin/', admin.site.urls),
]

