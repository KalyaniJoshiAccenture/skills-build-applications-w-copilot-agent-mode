"""octofit_tracker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from rest_framework import routers
from .views import UserViewSet, TeamViewSet, ActivityViewSet, WorkoutViewSet, LeaderboardViewSet
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
import os

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'teams', TeamViewSet)
router.register(r'activities', ActivityViewSet)
router.register(r'workouts', WorkoutViewSet)
router.register(r'leaderboards', LeaderboardViewSet)


# Helper to build the full API URL using $CODESPACE_NAME
def build_api_url(component):
    codespace_name = os.environ.get('CODESPACE_NAME', 'localhost')
    # Use HTTPS for codespace, HTTP for localhost
    if codespace_name == 'localhost':
        base_url = f"http://localhost:8000/api/{component}/"
    else:
        base_url = f"https://{codespace_name}-8000.app.github.dev/api/{component}/"
    return base_url

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': build_api_url('users'),
        'teams': build_api_url('teams'),
        'activities': build_api_url('activities'),
        'workouts': build_api_url('workouts'),
        'leaderboards': build_api_url('leaderboards'),
    })

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('', api_root, name='api-root'),
]
