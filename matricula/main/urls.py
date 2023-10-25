"""
URL configuration for main project.

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
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path
from aluno.views import aluno_criar, index, aluno_listar, aluno_editar, aluno_remover
from users.views import login_view, logout_view, create_user

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('aluno/', aluno_criar, name='aluno_criar'),
    path('aluno/editar/<int:id>/', aluno_editar, name='aluno_editar'),
    path('aluno/remover/<int:id>/', aluno_remover, name='aluno_remover'),
    path('aluno/listar', aluno_listar, name='aluno_listar'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('create_user/', create_user, name='create_user'),
]



