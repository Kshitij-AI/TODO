"""
URL configuration for TODO project.

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
from . import views

urlpatterns = [
    path('', views.homepage, name="home"),
    path('addTask/', views.addTask, name="taskAdd"),
    path('done/<int:pk>', views.markAsDone, name="taskDone"),
    path('undone/<int:pk>', views.markAsUndone, name="taskUndone"),
    path('delete/<int:pk>', views.deleteTask, name="taskDelete"),
    path('update/<int:pk>', views.updateTask, name="taskUpdate"),
]
