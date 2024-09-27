

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
router.register(r'carbon-credit', CarbonCreditViewSet)
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
