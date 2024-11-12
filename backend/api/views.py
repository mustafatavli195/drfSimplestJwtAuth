from django.contrib.auth.models import User
from .serializers import UserSerializer
from rest_framework.permissions import IsAuthenticated , AllowAny
from rest_framework import generics 
from rest_framework.views import APIView 
from rest_framework_simplejwt.views import TokenObtainPairView , TokenRefreshView
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from rest_framework import status

class LoginView(APIView):
    permission_classes = [AllowAny]
    
    def post(self , request):
        username = request.data.get("username")
        password = request.data.get("password")
        
        user = authenticate(username=username, password=password)
        
        if user is not None:
            refresh = RefreshToken.for_user(user)
            return Response({
                "refresh": str(refresh),
                "access": str(refresh.access_token),
            })
        else:
            return Response({"detail":"Invalid credentials"} , status=status.HTTP_401_UNAUTHORIZED)



#class CreateUserView(generics.CreateAPIView):
#    queryset = User.objects.all()
#    serializer_class = UserSerializer
#    permission_classes = [AllowAny]

class CreateUserView(APIView):
    permission_classes = [AllowAny]
    
    def post(self , request , *args, **kwargs):
        serializer = UserSerializer(data=request.data)
        
        if serializer.is_valid():
            user = serializer.save()
            
            return Response({
                "message":"User created successfully",
                "User": UserSerializer(user).data
            } , status=status.HTTP_201_CREATED)
        else:
            print(serializer.errors)
            return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)


#class CustomTokenObtainPairView(TokenObtainPairView):
#    permission_classes = [AllowAny]
#

class CustomTokenObtainPairView(APIView):
    permission_classes = [AllowAny]
    
    def post(self , request , *args, **kwargs):
        username = request.data.get("username")
        password = request.data.get("password")
        
        user = authenticate(username = username , password = password)
        if user is not None:
            return Response({"detail": "Invalid credentials."}, status=status.HTTP_401_UNAUTHORIZED)
        
        refresh = RefreshToken.for_user(user)
        access_token = str(refresh.access_token)
        refresh_token = str(refresh)
        
        return Response({
            "access": access_token,
            "refresh": refresh_token
        }, status=status.HTTP_200_OK)

    
#class TokenRefreshView(TokenRefreshView):
#   permission_classes = [AllowAny]


class CustomTokenRefreshView(APIView):
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        refresh_token = request.data.get("refresh") #Nasıl alıyor şuan requestin datası ne

        if not refresh_token:
            return Response({"detail": "Refresh token is required."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            refresh = RefreshToken(refresh_token)
            access_token = str(refresh.access_token)
            return Response({
                "access": access_token
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"detail": str(e)}, status=status.HTTP_400_BAD_REQUEST)