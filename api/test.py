# # api/tests.py (this isn't updated.)

# from django.test import TestCase
# import datetime
# from django.contrib.auth.models import User
# from rest_framework.test import APIClient
# from rest_framework import status
# from .models import SustainabilityGoal, CarbonFootprint, SustainableActs, EcoChallenge, ParticipationChallenge

# #this test class evaluates the basic working configuration of SustainablilityAPITest. (Deprecated)
# class SustainabilityAPITestCase(TestCase):
#     def setUp(self):
#         self.client = APIClient()
#         self.user = User.objects.create_user(username='testuser', password='testpass123')
#         self.client.force_authenticate(user=self.user)

#     def test_create_sustainability_goal(self):
#         data = {
#             'title': 'Reduce plastic waste',
#             'description': 'Minimize single-use plastic consumption',
#             'target_date': '2024-12-31'
#         }
#         response = self.client.post('/api/goals/', data)
#         print(f"status code: {response.status_code} and data: {response.data}")
#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)
#         self.assertEqual(SustainabilityGoal.objects.count(), 1)
#         self.assertEqual(SustainabilityGoal.objects.get().title, 'Reduce plastic waste')

#     def test_create_carbon_footprint(self):
#         data = {
#             'user': self.user.id,
#             'date': '2024-09-03',
#             'transportation_emissions': 5.2,
#             'consumption_of_energy': 10.5,
#             'generated_waste': 2.3
#         }
#         response = self.client.post('/api/carbon-footprints/', data)
#         print(f"status code: {response.status_code} and data: {response.data}")
#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)
#         self.assertEqual(CarbonFootprint.objects.count(), 1)
#         self.assertEqual(CarbonFootprint.objects.get().transportation_emissions, 5.2)

#     def test_create_sustainable_action(self):
#         data = {
#             'user': self.user.id,
#             'action_type': 'Recycling',
#             'description': 'Recycled paper and plastic bottles',
#             'impact_score': 8,
#             'date_performed': '2024-09-03'
#         }
#         response = self.client.post('/api/sustainable-acts/', data)
#         print(f"status code: {response.status_code} and data: {response.data}")
#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)
#         self.assertEqual(SustainableActs.objects.count(), 1)
#         self.assertEqual(SustainableActs.objects.get().action_type, 'Recycling')

#     def test_join_eco_challenge(self):
#         challenge = EcoChallenge.objects.create(
#             title='30-Day Zero Waste Challenge',
#             description='Reduce your waste for 30 days',
#             start_date=datetime.date.today(),#'2024-10-01',
#             end_date=datetime.date.today() + datetime.timedelta(days=30)
#         )

#         participation = ParticipationChallenge.objects.create(user=self.user, challenge=challenge)
#         self.assertIsNotNone(participation)
#         # response = self.client.post(f'/api/participations-challenge/', {'challenge': challenge.id})
#         #define test data
#         data = {
#             'user':self.user.id,
#             'challenge': challenge.id
#         }
#         #response
#         response = self.client.post('/api/participations-challenge/',data)
#         print(f"status code: {response.status_code} and data: {response.data}")
#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)
#         self.assertEqual(challenge.participants.count(), 1)
#         self.assertEqual(challenge.participants.first(), self.user)

#     def test_list_sustainability_goals(self):
#         SustainabilityGoal.objects.create(
#             title='Reduce energy consumption',
#             description='Lower household energy use',
#             target_date='2024-12-31'
#         )
#         response = self.client.get('/api/goals/')
#         # print(f"status code: {response.status_code} and data: {data}")
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertEqual(len(response.data), 1)
#         self.assertEqual(response.data[0]['title'], 'Reduce energy consumption')

#     # Add more test methods for other API endpoints and functionalities