from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views


# Create a router and register our ViewSets with it.
router = DefaultRouter()
router.register('list', views.TransactionViewset)


# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
    path('deposit/', views.DepositMoneyViewSet.as_view(), name='deposite'),
    path('reservation/', views.ReservationView.as_view(), name='reservation'),
   
]