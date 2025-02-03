from django.urls import path
from api.views import DoctorAPIView, NewsAPIView, DoctorSearchList, RegisterAPIView, LoginAPIView, DoctorUpdateAPIView, UserUpdateAPIView, UsersList

urlpatterns = [
    path('register', RegisterAPIView.as_view(), name='register'),  # for JWT token generation
    path('login', LoginAPIView.as_view(), name='login'),
    path('doctor', DoctorAPIView.as_view(), name='doctors-list'),
    path('doctor/<int:pk>', DoctorAPIView.as_view(), name='doctors-detail'),
    path('doctor/update/<int:pk>', DoctorUpdateAPIView.as_view(), name='doctor-update'),
    path('user/update/<int:pk>', UserUpdateAPIView.as_view(), name='user-update'),
    path('users', UsersList.as_view(), name='users-list'),
    path('search', DoctorSearchList.as_view(), name='search'),
    path('news', NewsAPIView.as_view(), name='news-list'),
    path('news/<int:pk>', NewsAPIView.as_view(), name='news-detail'),
]
