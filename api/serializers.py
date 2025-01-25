from rest_framework import serializers
from .models import Doctor, User, News
from root import settings

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'role', 'first_name', 'last_name']

class UserSerializer(serializers.ModelSerializer):
    avatar = serializers.SerializerMethodField()
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'avatar']

    def get_avatar(self, obj):
        if obj.avatar:
            return settings.BASE_URL + obj.avatar.url
        return None


class DoctorSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Doctor
        fields = ['user','specialization','experience','location','clinic_name','consultation_fee','is_consultation_free','availability_today']





class NewsSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    image = serializers.SerializerMethodField()
    class Meta:
        model = News
        fields = ['user', 'user', 'title', 'image', 'created_at']

    def get_image(self, obj):
        if obj.image:
            return settings.BASE_URL + obj.image.url
        return None
