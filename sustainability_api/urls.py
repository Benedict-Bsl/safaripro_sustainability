"""
URL configuration for sustainability_api project.

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
from django.urls import path,include
from rest_framework.routers import DefaultRouter
# from api.views import SustainabilityGoalViewSet CarbonFootprintViewSet SustainableActViewSet EcoChallengeViewSet ParticipationChallengeViewSet SustainableCharityViewSet
from api.views import *

router = DefaultRouter()
#registering viewset as routing point for the api

router.register(r'goals',SustainabilityGoalViewSet)
router.register(r'carbon-footprints', CarbonFootprintViewSet)
router.register(r'sustainable-acts', SustainableActViewSet)
router.register(r'eco-challenges', EcoChallengeViewSet)
router.register(r'participations-challenge', ParticipationChallengeViewSet)
router.register(r'sustainable-charity', SustainableCharityViewSet)
router.register(r'donations',DonationsViewSet)
# router.register(r'conservations-org',ConservationOrgViewSet)
router.register(r'conservations-initiatives',ConservationInitViewSet)
router.register(r'articles', EducationArticleViewSet)
router.register(r'artists', ArtistViewSet)
router.register(r'artworks', WorkViewSet)

#registering url parterns
urlpatterns = [
    path("admin/", admin.site.urls),
    path('api/', include(router.urls)),
    path('',include('api.urls')),
]
