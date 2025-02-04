from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model
from rest_framework import status
from api.models import Doctor, News
from decimal import Decimal
from django.urls import reverse
import logging

logger = logging.getLogger(__name__)


class DoctorModelTest(APITestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            email="doctor@example.com",
            password="password123"
        )

        self.doctor = Doctor.objects.create(
            user=self.user,
            specialization="Cardiologist",
            experience=10,
            location="Tashkent",
            clinic_name="Healthy Life Clinic",
            consultation_fee=Decimal('100.00'),
            is_consultation_free=False,
            availability_today=True,
            rating_percentage=90,
            patient_stories=200
        )
        self.url = reverse('doctors-list')
        self.url_detail = reverse('doctors-detail', kwargs={'pk': self.doctor.pk})
        self.client.login(username=self.user.email, password="password123")

    def test_create_doctor(self):
        doctor = self.doctor
        self.assertEqual(doctor.specialization, "Cardiologist")
        self.assertEqual(doctor.experience, 10)
        self.assertEqual(doctor.location, "Tashkent")
        self.assertEqual(doctor.clinic_name, "Healthy Life Clinic")
        self.assertEqual(doctor.consultation_fee, Decimal('100.00'))
        self.assertEqual(doctor.is_consultation_free, False)
        self.assertEqual(doctor.availability_today, True)
        logger.info("\nTest 1 (Doctors-create) ✅\n")

    def test_get_doctors(self):
        response = self.client.get(self.url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['specialization'], "Cardiologist")
        self.assertEqual(response.data[0]['experience'], 10)
        self.assertEqual(response.data[0]['location'], "Tashkent")
        self.assertEqual(response.data[0]['clinic_name'], "Healthy Life Clinic")
        self.assertEqual(str(response.data[0]['consultation_fee']), '100.00')
        self.assertEqual(response.data[0]['is_consultation_free'], False)
        self.assertEqual(response.data[0]['availability_today'], True)
        logger.info("\nTest 2 (Doctors-list) ✅\n")

    def test_get_doctor_detail(self):
        response = self.client.get(self.url_detail)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['specialization'], "Cardiologist")
        self.assertEqual(response.data['experience'], 10)
        self.assertEqual(response.data['location'], "Tashkent")
        self.assertEqual(response.data['clinic_name'], "Healthy Life Clinic")
        self.assertEqual(str(response.data['consultation_fee']), '100.00')
        self.assertEqual(response.data['is_consultation_free'], False)
        self.assertEqual(response.data['availability_today'], True)
        logger.info("\nTest 3 (Doctors-details) ✅\n")


class NewsModelTestCase(APITestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            email="news@example.com",
            password="password123"
        )
        self.news = News.objects.create(
            user=self.user,
            title="Healthy Life News",
            image="/news/multicoders.jpg"
        )
        self.url = reverse('news-list')
        self.url_detail = reverse('news-detail', kwargs={'pk': self.news.pk})
        self.client.login(username=self.user.email, password="password123")

    def test_create_news(self):
        news = self.news

        self.assertEqual(news.title, "Healthy Life News")
        self.assertEqual(news.image, "/news/multicoders.jpg")
        logger.info("\nTest 4 (News-create) ✅\n")

    def test_get_news(self):
        response = self.client.get(self.url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], "Healthy Life News")
        self.assertEqual(response.data[0]['image'], "/media/news/multicoders.jpg")
        logger.info("\nTest 5 (News-list) ✅\n")
