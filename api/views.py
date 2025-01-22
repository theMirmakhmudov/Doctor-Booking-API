from api.models import Doctor
from api.serializers import DoctorSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class DoctorAPIView(APIView):
    def get(self,request,pk=None):
        if pk:
            try:
                doctor = Doctor.objects.get(pk=pk)
                serializer = DoctorSerializer(doctor)
                return Response(serializer.data)
            except:
                return Response({'error':'Doctor does not exist'}, status=status.HTTP_404_NOT_FOUND)
        else:
            doctor= Doctor.objects.all()
            serializer = DoctorSerializer(doctor,many=True)
            return Response(serializer.data)
