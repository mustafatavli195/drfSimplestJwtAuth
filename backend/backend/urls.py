from django.contrib import admin
from django.urls import path , include
from api.views import CreateUserView , LoginView , CustomTokenObtainPairView , CustomTokenRefreshView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/user/register/" , CreateUserView.as_view() , name="create"),
    path("api-auth/" , include("rest_framework.urls")),
    path("api/token/" , CustomTokenObtainPairView.as_view() , name="token"),
    path("api/token/refresh/" , CustomTokenRefreshView.as_view() , name="refresh"),
    path("api/user/login/" , LoginView.as_view() , name="login"),
]
