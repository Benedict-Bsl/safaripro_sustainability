from rest_framework import viewsets
from rest_framework.response import Response
from .models import *
from .serializers import *

# UserSerializer SustainabilityGoalSerializer CarbonFootprintSerializer SustainableActSerializer EcoChallengeSerializer ParticipationChallengeSerializer SustainableCharitySerializer

#list of viewSet Classes for each route.
class SustainabilityGoalViewSet(viewsets.ModelViewSet):
    queryset = SustainabilityGoal.objects.all()
    serializer_class = SustainabilityGoalSerializer

class CarbonFootprintViewSet(viewsets.ModelViewSet):
    queryset = CarbonFootprint.objects.all()
    serializer_class = CarbonFootprintSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class SustainableActViewSet(viewsets.ModelViewSet):
    queryset = SustainableActs.objects.all()
    serializer_class = SustainableActSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class EcoChallengeViewSet(viewsets.ModelViewSet):
    queryset = EcoChallenge.objects.all()
    serializer_class = EcoChallengeSerializer


class ParticipationChallengeViewSet(viewsets.ModelViewSet):
    queryset = ParticipationChallenge.objects.all()
    serializer_class = ParticipationChallengeSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class SustainableCharityViewSet(viewsets.ModelViewSet):
    queryset = SustainableCharity.objects.all()
    serializer_class = SustainableCharitySerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class ConservationInitViewSet(viewsets.ModelViewSet):
    queryset = ConservationInitiatives.objects.all()
    serializer_class = ConservationInitSerializer
    
    #accessing/accessing image values
    def list(self,request,*args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset,many=True)

        data = serializer.data 
        
        return Response(data)

class DonationsViewSet(viewsets.ModelViewSet):
    queryset = Donations.objects.all()
    serializer_class=DonationSerializer

class EducationArticleViewSet(viewsets.ModelViewSet):
    queryset = EducationArticle.objects.all()
    serializer_class = EducationArticleSerializer
    # permission_classes = [IsAuthenticatedOrReadOnly]

class ArtistViewSet(viewsets.ModelViewSet):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer

class WorkViewSet(viewsets.ModelViewSet):
    queryset = ArtWork.objects.all()
    serializer_class = WorkSerializer