
from rest_framework import status
from rest_framework.authtoken.views import  APIView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

from django.contrib.auth import logout

from .serializers import AdminSerializer, JobSeekerSerializer, JobSerializer
from .models import Admin, JobSeeker, Job

class AdminAPIView(APIView):

    def post(self, request):
        serializer = AdminSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            refresh = RefreshToken.for_user(user)
            token = {
                    'refresh': str(refresh),
                    'access': str(refresh.access_token),
                }
            return Response({'message':'User registered successfully',
                            'token': token
                            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class JobSeekerAPIView(APIView):
    
    def post(self, request):
       
        serializer = JobSeekerSerializer(data=request.data)
        
        if serializer.is_valid():
            user = serializer.save()
            refresh = RefreshToken.for_user(user)
            token = {
                    'refresh': str(refresh),
                    'access': str(refresh.access_token),
                }
            return Response({'message':'User registered successfully',
                            'token': token
                            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class JobAPIView(APIView):
    
    def post(self, request):
        serializer = JobSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            refresh = RefreshToken.for_user(user)
            token = {
                    'refresh': str(refresh),
                    'access': str(refresh.access_token),
                }
            return Response({'message':'User registered successfully',
                            'token': token
                            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class LogoutView(APIView):
    def post(self, request):
        logout(request)
        return Response({"detail": "Logged out successfully"})

'''
class RegisterView(APIView):
    
    def post(self, request):

        if request.data.get('groups') == [1]:
            serializer = JobSeekerSerializer(data=request.data)
            if serializer.is_valid(raise_exception=True):
                user = serializer.save()
                serializer_data = serializer.data
                serializer_data['user_permissions'] = [20, 28, 32]
                refresh = RefreshToken.for_user(user)
                token = {
                    'refresh': str(refresh),
                    'access': str(refresh.access_token),
                }
                return Response({'message':'User registered successfully',
                                'token': token
                            }, status=status.HTTP_201_CREATED)
            return Response({'message': 'Invalid User'}, status=status.HTTP_400_BAD_REQUEST)

        elif request.data.get('groups') == [2]:
            serializer = JobGiverSerializer(data=request.data)
            if serializer.is_valid(raise_exception=True):
                user = serializer.save()
                serializer_data = serializer.data
                serializer_data['user_permissions'] = [8, 20, 28, 32]
                refresh = RefreshToken.for_user(user)
                token = {
                    'refresh': str(refresh),
                    'access': str(refresh.access_token),
                }
                return Response({'message':'User registered successfully',
                                'token': token
                            }, status=status.HTTP_201_CREATED)
            return Response({'message': 'Invalid User'}, status=status.HTTP_400_BAD_REQUEST)
        
        
        else:
            return Response({'message': 'Group does not exist'}, status=status.HTTP_400_BAD_REQUEST)
        

class AdminRegisterView(APIView):
    def post(self, request):
        serializer = AdminSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
            refresh = RefreshToken.for_user(user)
            token = {
                    'refresh': str(refresh),
                    'access': str(refresh.access_token),
                }
            return Response({'message':'User registered successfully',
                                'token': token
                            }, status=status.HTTP_201_CREATED)
        return Response({'message': 'Invalid User'}, status=status.HTTP_400_BAD_REQUEST)


class LogoutView(APIView):
    def post(self, request):
        logout(request)
        return Response({"detail": "Logged out successfully"})
'''