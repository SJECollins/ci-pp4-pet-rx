"""petrx URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('vetprofiles.urls'), name='vetprofile_urls'),
    path('prescriptions/', include('prescriptions.urls'),
         name='prescriptions_urls'),
    path('records/', include('records.urls'), name='records_urls'),
]


handler403 = "vetprofiles.views.handle_403"
handler404 = "vetprofiles.views.handle_404"
handler405 = "vetprofiles.views.handle_405"
handler500 = "vetprofiles.views.handle_500"
