"""music_prj URL Configuration

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
from allauth.account.views import confirm_email
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from musicApp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.new_index, name='new_index'),
    path('new_index', views.new_index, name='new_index'),

    path('genre', views.genre, name='genre'),
    path('filtering', views.filtering, name='filtering'),
    path('mypage', views.mypage, name='mypage'),
    path('new_index', views.new_index, name='new_index'),
    path('playlist', views.playlist, name='playlist'),
    path('tag', views.tag, name='tag'),
    path('test', views.test, name='test'),
    path('team', views.team, name='team'),
    path('registerProfile/', include('registerProfile.urls', namespace='registerProfile')),

    # 소셜 로그인
    path('account/login/kakao/', views.kakao_login, name='kakao_login'),
    path('account/logout/kakao/', views.kakao_logout, name='kakao_logout'),
    path('account/login/kakao/callback/', views.kakao_callback, name='kakao_callback'),

]
