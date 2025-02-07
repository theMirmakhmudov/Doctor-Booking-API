from django.urls import path
from api.views import (
    RegisterAPIView,
    LoginAPIView,
    DoctorAPIView,
    DoctorDetailsAPIView,
    DoctorSearchList,
    DoctorDeleteAPIView,
    DoctorUpdateAPIView,
    NewsAPIView,
    NewsDetailsAPIView,
    UserUpdateAPIView,
    UsersList,
    DoctorDateAPIView,
    BookingAPIView,

)

urlpatterns = [
    path('register', RegisterAPIView.as_view(), name='register'),  # for JWT token generation
    path('login', LoginAPIView.as_view(), name='login'),
    path('doctor', DoctorAPIView.as_view(), name='doctors-list'),
    path('doctor/<int:pk>', DoctorDetailsAPIView.as_view(), name='doctors-detail'),
    path('doctor/update/<int:pk>', DoctorUpdateAPIView.as_view(), name='doctor-update'),
    path('doctor/delete/<int:pk>', DoctorDeleteAPIView.as_view(), name='doctor-delete'),
    path('date', DoctorDateAPIView.as_view(), name='doctor-date'),
    path('booking/<int:pk>', BookingAPIView.as_view(), name='booking'),
    path('booking/<int:pk>', BookingAPIView.as_view(), name='booking-detail'),
    path('user/update/<int:pk>', UserUpdateAPIView.as_view(), name='user-update'),
    path('users', UsersList.as_view(), name='users-list'),
    path('search', DoctorSearchList.as_view(), name='search'),
    path('news', NewsAPIView.as_view(), name='news-list'),
    path('news/<int:pk>', NewsDetailsAPIView.as_view(), name='news-detail'),
]
