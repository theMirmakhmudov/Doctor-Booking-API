from django.urls import path
from api.views import DoctorAPIView, NewsAPIView, DoctorSearchList, RegisterAPIView

urlpatterns = [
    path('register', RegisterAPIView.as_view(), name='register'),  # for JWT token generation
    path('doctor', DoctorAPIView.as_view(), name='doctors-list'),
    path('doctor/<int:pk>', DoctorAPIView.as_view(), name='doctors-detail'),
    path('search', DoctorSearchList.as_view(), name='search'),
    path('news', NewsAPIView.as_view(), name='news-list'),
    path('news/<int:pk>', NewsAPIView.as_view(), name='news-detail'),
]
