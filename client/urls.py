from django.urls import path, include
from rest_framework.routers import DefaultRouter
from django.conf import settings 
from django.conf.urls.static import static
from . views import ClientViewset, UserRegistrationAPIView, UserLoginAPIView, UserLogoutView

# Create a router and register our ViewSets with it.
router = DefaultRouter()
router.register('list', ClientViewset)


# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
    path('register/', UserRegistrationAPIView.as_view(), name='register'),
    path('login/', UserLoginAPIView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
]