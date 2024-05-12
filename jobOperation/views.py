from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .models import PersonalData,  JobData, AdminContent
from .serializers import PersonalDataSerializer, JobGiverSerializer, AdminContentSerializer
from django.http import Http404

class PersonalDataListAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        request.data['job_seeker'] = request.user.id
        serializer = PersonalDataSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def get_object(self, pk):
        try:
            return PersonalData.objects.get(job_seeker=pk)
        except PersonalData.DoesNotExist:
            raise Http404

    def get(self, request):
        personal_data = self.get_object(request.user.id)
        serializer = PersonalDataSerializer(personal_data)
        return Response(serializer.data)

    def put(self, request):
        personal_data = self.get_object(request.user.id)
        serializer = PersonalDataSerializer(personal_data, data=request.data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        personal_data = self.get_object(request.user.id)
        personal_data.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class JobDataView(APIView):

    permission_classes = [IsAuthenticated]
    def post(self, request):
        request.data['job_giver'] = request.user.id
        serializer = JobGiverSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def get_object(self, pk):
        try:
            return JobData.objects.get(job_giver=pk)
        except JobData.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
    
    def get(self, request):
        job_giver = self.get_object(request.user.id)
        serializer = JobGiverSerializer(job_giver)
        return Response(serializer.data)

    def put(self, request):
        job_giver = self.get_object(request.user.id)
        serializer = JobGiverSerializer(job_giver, data=request.data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        job_giver = self.get_object(request.user.id)
        job_giver.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class AdminContentView(APIView):
    
    def post(self, request):
        request.data['app_admin'] = request.user.id
        serializer = AdminContentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get_object(self, pk):
        try:
            return AdminContent.objects.get(app_admin=pk)
        except AdminContent.DoesNotExist:
            raise Http404

    def get(self, request):
        admin_content = self.get_object(request.user.id)
        serializer = AdminContentSerializer(admin_content)
        return Response(serializer.data)

    def put(self, request):
        admin_content = self.get_object(request.user.id)
        serializer = AdminContentSerializer(admin_content, data=request.data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        admin_content = self.get_object(request.user.id)
        admin_content.delete()
        return Response(status=status.HTTP_204_NO_CONTENT) 
