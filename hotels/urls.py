from django.urls import path, include
from rest_framework.routers import DefaultRouter
from django.conf import settings 
from django.conf.urls.static import static
from . import views

# Create a router and register our ViewSets with it.
router = DefaultRouter()
router.register('list', views.HotelViewset)
router.register('review', views.ReviewViewset)

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.HOTELS_MEDIA_ROOT)