"""gladier_ptycho_portal URL Configuration

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
from django.conf import settings
from globus_portal_framework.urls import register_custom_index
from gladier_ptycho_portal.views import (
    GlobusPilotSearchView,
)



app_name = 'gladier-ptychography-portal'
register_custom_index('ptychography_index', ['ptycho'])


urlpatterns = [
    path('admin/', admin.site.urls),
    path('<ptychography_index:index>/', GlobusPilotSearchView.as_view(), name='search'),
]

if 'ALCF' not in settings.PROJECT_TITLE:
    urlpatterns += [
        path('', include('social_django.urls', namespace='social')),
        path('', include('globus_portal_framework.urls')),
    ]