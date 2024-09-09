#importing libraries
from django.db import models
from django.contrib.auth.models import User 
from django.utils.text import slugify 
from django.core.validators import *

#class defining sustainability goals
class SustainabilityGoal(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    target_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
#class difining statainable charity
class SustainableCharity(models.Model):
    title = models.CharField(max_length=100)
    charity_description = models.TextField()
    charity_actions = models.TextField()

    def __str__(self):
        return self.title 
#class for carbon footPrinting track
class CarbonFootprint(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    transportation_emissions = models.FloatField()
    consumption_of_energy = models.FloatField()
    generated_waste = models.FloatField()
    creation_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username}'s Carbon Footprint on {self.date}"

class SustainableActs(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    action_type = models.CharField(max_length=50)
    description = models.TextField()
    impact_score = models.IntegerField()
    date_performed = models.DateField()
    creation_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username}'s {self.action_type} on {self.date_performed}"

#class describing economical/ ecological challenges
class EcoChallenge(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    end_date = models.DateField()
    participants = models.ManyToManyField(User,through='ParticipationChallenge')
    creation_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title 

#class recording challenges participation
class ParticipationChallenge(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    challenge = models.ForeignKey(EcoChallenge, on_delete=models.CASCADE,null=True)
    join_date = models.DateField(auto_now_add=True)
    completion_date = models.DateField(null=True, blank=True)
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username}'s participation in {self.challenge.title}"

#Conservation efforts for sustainable developments
class ConservationInitiatives(models.Model):

    name = models.CharField(max_length=255, unique=True)
    location = models.CharField(max_length=255)
    description = models.TextField()
    mission = models.TextField(blank=True)
    target_fund_raise = models.FloatField(blank=True,default=0)
    current_funds = models.FloatField(blank=True,default=0)
    number_of_donors = models.PositiveIntegerField(blank=True,default=0)
    email = models.EmailField(validators=[EmailValidator()], blank=True,default="example@gmai.com")

    #storin images to appwriteServer
    images = models.ImageField(blank=True)
    contact_info = models.TextField()
    website = models.URLField(validators=[URLValidator()], blank=True)
    slug = models.SlugField(unique=True, editable=False)
    date_of_creation = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name 
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug=slugify(self.name)
        super().save(*args, **kwargs)

#donations
class Donations(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    beneficiary_name = models.TextField()
    beneficiary_contact = models.TextField()
    donation_date = models.DateTimeField(auto_now=True)
    donation_amount = models.FloatField(default=0)

    def __str__(self):
        return self.beneficiary_name

#Education
class EducationArticle(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, max_length=255)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    published_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=[('draft', 'Draft'), ('published', 'Published')], default='draft')
    featured_image = models.ImageField(upload_to='articles/', null=True, blank=True)
    tags = models.CharField(max_length=255, blank=True)
    is_featured = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-published_date']

    @property
    def featured_image_url(self):
        """Return the full URL of the featured image."""
        if self.featured_image:
            return self.featured_image.url
        return None
class Artist(models.Model):
    artist_name = models.CharField(max_length=255)
    bio = models.TextField(blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)
    nationality = models.CharField(max_length=100, blank=True, null=True)
    profile_picture = models.ImageField(upload_to='artists/', blank=True, null=True)  # Keep this to upload images

    def __str__(self):
        return self.artist_name

    @property
    def profile_picture_url(self):
        if self.profile_picture:
            return self.profile_picture.url
        return None

class ArtWork(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name='works')
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    creation_date = models.DateField(blank=True, null=True)
    donation_amount = models.DecimalField(max_digits=10, decimal_places=2)  # Stores monetary donation amount
    artwork_image = models.ImageField(upload_to='works/', blank=True, null=True)  # Keep this to upload images

    def __str__(self):
        return f"{self.title} by {self.artist.artist_name}"

    @property
    def artwork_image_url(self):
        if self.artwork_image:
            return self.artwork_image.url
        return None
