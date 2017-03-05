"""web2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from search import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^\?(?P<code>code=[0-9]+)$', views.fetch, name='fetch'),
    url(r'^\?(?P<code>code=[0-9]+)(?P<alt_crime>&alt_crime=[0-9]+)(?P<alt_school>&alt_school=[0-9]+)(?P<alt_income>&alt_income=[0-9]+)(?P<alt_cta>&alt_cta=[0-1])$',
        views.alter, name='alter')
]
