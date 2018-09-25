"""trafficforcast URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
import rest_framework_swagger
from django.contrib import admin
from django.urls import path
from api.views import get_all_post, push_post, get_all_road_data, get_road_data
from api import views

urlpatterns = [
    path('admin/', admin.site.urls),

    #Rest
    path('api/getAllPost/', get_all_post.as_view()),
    path('api/pushPost/', push_post.as_view()),
    path('api/test/', views.test_post),
    path('api/getAllRoadData/', get_all_road_data.as_view()),
    path('api/getRoadData/', get_road_data.as_view()),
    path('api/saveRoadData/', views.save_road_data),
]
