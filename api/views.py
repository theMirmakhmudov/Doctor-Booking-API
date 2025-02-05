from django.shortcuts import get_object_or_404
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.throttling import AnonRateThrottle, UserRateThrottle
from api.models import Doctor, News, User, Booking
from api.serializers import (
    RegisterSerializer,
    LoginSerializer,
    DoctorSerializer,
    DoctorUpdateSerializer,
    NewsSerializer,
    UserUpdateSerializer,
    UserSerializer,
    BookingSerializer
)
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.hashers import make_password, check_password
from rest_framework.permissions import IsAuthenticated
from drf_spectacular.utils import extend_schema, OpenApiParameter
from rest_framework.parsers import MultiPartParser, FormParser


class RegisterAPIView(APIView):
    @extend_schema(
        summary="User Registration",
        description="Register user",
        request=RegisterSerializer,
        responses={
            200: OpenApiParameter(name="Tokens", description="JWT access token and refresh tokens"),
            400: OpenApiParameter(name="Errors", description="Invalid credentials")
        },
        tags=["User Authentication"]
    )
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save(password=make_password(serializer.validated_data['password']))
            # Generate JWT token
            refresh = RefreshToken.for_user(user)
            access_token = str(refresh.access_token)

            return Response(
                {
                    "refresh": str(refresh),
                    "access": access_token
                }, status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginAPIView(APIView):
    @extend_schema(
        summary="User Login",
        description="Login user with email and password",
        request=LoginSerializer,
        responses={
            200: OpenApiParameter(name="Tokens", description="JWT access token and refresh tokens"),
            400: OpenApiParameter(name="Errors", description="Invalid credentials")
        },
        tags=["User Authentication"]
    )
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data['email']
            password = serializer.validated_data['password']
            if user and check_password(password, User.objects.get(email=user).password):
                # Generate JWT token
                refresh = RefreshToken.for_user(User.objects.get(email=user))
                access_token = str(refresh.access_token)

                return Response(
                    {
                        "refresh": str(refresh),
                        "access": access_token
                    }, status=status.HTTP_200_OK
                )
            else:
                return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)


class UsersList(APIView):
    def get(self, request):
        try:
            user = User.objects.all()
            serializer = UserSerializer(user, many=True)
            return Response(serializer.data)
        except:
            return Response({'error': 'News does not exist'}, status=status.HTTP_404_NOT_FOUND)


class UserUpdateAPIView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    @extend_schema(
        summary="User Registration",
        description="Register user",
        request=UserUpdateSerializer,
        responses={
            200: OpenApiParameter(name="User Updated", description="User data updated"),
            400: OpenApiParameter(name="Errors", description="Invalid credentials")
        },
        tags=["User Update"]
    )
    def put(self, request, pk):
        user = get_object_or_404(User, pk=pk)
        serializer = UserUpdateSerializer(instance=user, data=request.data, partial=False)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "User updated successfully"}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DoctorAPIView(APIView):
    permission_classes = [IsAuthenticated]
    throttle_classes = (AnonRateThrottle, UserRateThrottle)

    @extend_schema(
        summary="Doctors Information",
        description="Doctor API View",
        tags=["Doctor"])
    def get(self, request):
        doctor = Doctor.objects.all()
        serializer = DoctorSerializer(doctor, many=True)
        return Response(serializer.data)


class DoctorDetailsAPIView(APIView):
    def get(self, request, pk):
        try:
            doctor = Doctor.objects.get(pk=pk)
            serializer = DoctorSerializer(doctor)
            return Response(serializer.data)
        except:
            return Response({'error': 'Doctor does not exist'}, status=status.HTTP_404_NOT_FOUND)


class DoctorSearchList(generics.ListAPIView):
    serializer_class = DoctorSerializer
    queryset = Doctor.objects.all()
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['location', 'clinic_name']
    filterset_fields = ['experience', 'rating_percentage', 'location', 'clinic_name']


class DoctorUpdateAPIView(APIView):
    @extend_schema(
        summary="Doctor Update API View",
        description="Doctor Update Data",
        request=DoctorUpdateSerializer,
        responses={
            200: OpenApiParameter(name="Doctor Update", description="Doctor Update APi View data"),
            400: OpenApiParameter(name="Errors", description="Invalid credentials")
        },
        tags=["Doctor"]
    )
    def put(self, request, pk):
        doctor = get_object_or_404(Doctor, pk=pk)
        serializer = DoctorUpdateSerializer(doctor, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DoctorDeleteAPIView(APIView):
    def delete(self, request, pk):
        doctor = get_object_or_404(Doctor, pk=pk)
        doctor.delete()
        return Response({'message': 'Doctor has been deleted successfully'}, status=status.HTTP_200_OK)


class NewsAPIView(APIView):
    throttle_classes = (AnonRateThrottle, UserRateThrottle)

    @extend_schema(
        summary="News Information",
        description="News API View",
        tags=["News"])
    def get(self, request):
        try:
            news = News.objects.all()
            serializer = NewsSerializer(news, many=True)
            return Response(serializer.data)
        except:
            return Response({'error': 'News does not exist'}, status=status.HTTP_404_NOT_FOUND)


class NewsDetailsAPIView(APIView):
    def get(self, request, pk):
        try:
            news = News.objects.get(pk=pk)
            serializer = NewsSerializer(news)
            return Response(serializer.data)
        except:
            return Response({'error': 'News does not exist'}, status=status.HTTP_404_NOT_FOUND)


class BookingAPIView(APIView):
    def get(self, request):
        booking = Booking.objects.all()
        serializer = BookingSerializer(booking, many=True)
        return Response(serializer.data)
