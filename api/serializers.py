from rest_framework import serializers
from .models import Doctor


class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = ['specialization','experience','location','clinic_name','consultation_fee','is_consultation_free','availability_today']
