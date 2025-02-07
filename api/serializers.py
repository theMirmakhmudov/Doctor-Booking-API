from rest_framework import serializers
from .models import Doctor, User, News, Date
from root import settings


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'role', 'first_name', 'last_name']


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'avatar']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        if instance.avatar:
            representation['avatar'] = settings.BASE_URL + instance.avatar.url
        else:
            representation['avatar'] = None
        return representation


class UserUpdateSerializer(serializers.ModelSerializer):
    avatar = serializers.ImageField()

    class Meta:
        model = User
        fields = ["first_name", "last_name", "avatar"]


class DoctorSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Doctor
        fields = ['user', 'id', 'specialization', 'experience', 'location', 'clinic_name', 'consultation_fee',
                  'is_consultation_free', 'availability_today']

        def update(self, instance, validated_data):
            user_data = validated_data.pop('user', None)

            for attr, value in validated_data.items():
                setattr(instance, attr, value)
            instance.save()

            if user_data:
                user_instance = instance.user
                for attr, value in user_data.items():
                    setattr(user_instance, attr, value)
                user_instance.save()

            return instance


class DoctorUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = ['specialization', 'experience', 'location', 'clinic_name', 'consultation_fee',
                  'is_consultation_free', 'availability_today']


class NewsSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = News
        fields = ['user', 'user', 'title', 'image', 'created_at']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        if instance.image:
            representation['image'] = settings.BASE_URL + instance.image.url
        else:
            representation['image'] = None
        return representation

class DateSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Date
