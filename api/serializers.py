#converting models into data specific types
from rest_framework import serializers
from .models import SustainabilityGoal, CarbonFootprint, SustainableActs, ParticipationChallenge, EcoChallenge, SustainableCharity, Donations, ConservationInitiatives, EducationArticle, Artist, ArtWork,CarbonCredit
from django.contrib.auth.models import User

#serializing user data
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username','email']

class SustainabilityGoalSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = SustainabilityGoal
        fields = '__all__'

class CarbonFootprintSerializer(serializers.ModelSerializer):
    #serialize user data for carbon footprint
    user = UserSerializer(read_only=True)
    class Meta:
        model = CarbonFootprint
        fields = '__all__'
class SustainableActSerializer(serializers.ModelSerializer):
    #serializing sustainable acts
    user = UserSerializer(read_only=True)

    class Meta:
        model=SustainableActs
        fields = '__all__'

class EcoChallengeSerializer(serializers.ModelSerializer):
    #serialize participant data for challenge
    participants = UserSerializer(many=True, read_only=True)
    class Meta:
        model = EcoChallenge
        fields = '__all__'

class ParticipationChallengeSerializer(serializers.ModelSerializer):
    #serialize challege and user data for particiaption
    user = UserSerializer(read_only=True)
    challenge = EcoChallengeSerializer(read_only=True)
    class Meta:
        model = ParticipationChallenge
        fields = '__all__'

class SustainableCharitySerializer(serializers.ModelSerializer):
    #serialize user data for charity
    user = UserSerializer(read_only=True)
    class Meta:
        model = SustainableCharity
        fields = '__all__'

class DonationSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    class Meta:
        model = Donations
        fields = '__all__'

class ConservationInitSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    class Meta:
        model = ConservationInitiatives
        fields = '__all__'

class CarbonCreditSerializer(serializers.ModelSerializer):
    # user = UserSerializer(read_only=True)    
    class Meta:
        model = CarbonCredit
        fields = '__all__'


class EducationArticleSerializer(serializers.ModelSerializer):
    featured_image_url = serializers.SerializerMethodField()

    class Meta:
        model = EducationArticle
        fields = '__all__'

    def get_featured_image_url(self, obj):
        """Returns the full URL for the featured image."""
        request = self.context.get('request')
        if obj.featured_image:
            return request.build_absolute_uri(obj.featured_image.url)
        return None

class ArtistSerializer(serializers.ModelSerializer):
    profile_picture_url = serializers.SerializerMethodField()

    class Meta:
        model = Artist
        fields = fields = '__all__'

    def get_profile_picture_url(self, obj):
        request = self.context.get('request')
        if obj.profile_picture:
            return request.build_absolute_uri(obj.profile_picture.url)
        return None


class WorkSerializer(serializers.ModelSerializer):
    artist_id = serializers.PrimaryKeyRelatedField(queryset=Artist.objects.all(), source='artist')  # Include artist details in the work
    artist_name = serializers.CharField(source='artist.artist_name', read_only=True) 
    artwork_image_url = serializers.SerializerMethodField()
    artist_profile = serializers.ImageField(source='artist.profile_picture',read_only=True)
    artist_bio = serializers.CharField(source='artist.bio', read_only=True)
    
    class Meta:
        model = ArtWork
        fields = '__all__'

    def get_artwork_image_url(self, obj):
        request = self.context.get('request')
        if obj.artwork_image:
            return request.build_absolute_uri(obj.artwork_image.url)
        return None
    
    def create(self, validated_data):
        # Extract the artist from validated data
        artist = validated_data.pop('artist')

        # Create a new Work with the extracted artist and the rest of the validated data
        work = ArtWork.objects.create(artist=artist, **validated_data)

        return work
# class ConservationOrgSerializer(serializers.ModelSerializer):
#     user = UserSerializer(read_only=True)
#     class Meta:
#         model = ConservationOrganizations
#         fields = '__all__'
