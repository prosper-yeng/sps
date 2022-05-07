"""sps URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path,include
from rest_framework.schemas import get_schema_view
from rest_framework.documentation import include_docs_urls

urlpatterns = [
    path ( '', include_docs_urls ( title='API for SPS' ) ),
    path('', include(('person.urls', 'person'), namespace='person')),
    path ( '', include ( ('groups.urls', 'groups'), namespace='group' ) ),
    path ( '', include ( ('select_item.urls', 'select_item'), namespace='select_item' ) ),
    path ( '', include ( ('nation.urls', 'nation'), namespace='nation' )),
    path ( '', include ( ('region.urls', 'region'), namespace='region') ),
    path ( '', include ( ('district.urls', 'district'), namespace='district') ),
    path ( '', include ( ('constituency.urls', 'constituency'), namespace='constituency') ),
    path ( '', include ( ('electoral_area.urls', 'electoral_area'), namespace='electoral_area' ) ),
    path ( '', include ( ('polling_station.urls', 'polling_station'), namespace='polling_station') ),
    path('admin/', admin.site.urls),

    path ( 'schema', get_schema_view (
        title='API for SPS',
        description='API for SPS',
        version='1.0'
    ), name='openapi-schema'

           ),

]
