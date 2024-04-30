from rest_framework import serializers, status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.core.mail import EmailMultiAlternatives
from rest_framework import viewsets
from django.template.loader import render_to_string
from .models import Transaction
from . import serializers
from hotels.models import Hotel
from reservations.models import Reservations
from client.models import UserAccount

from reservations.serializers import ReservationsSerializer

class TransactionViewset(viewsets.ModelViewSet):
    queryset = Transaction.objects.all() 
    serializer_class = serializers.UserTransactionSerializer

    

class DepositMoneyViewSet(APIView):
    serializer_class = serializers.TransactionSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            amount = serializer.validated_data['amount']
            user = request.user

            try:
                account = UserAccount.objects.get(user=user)
            except UserAccount.DoesNotExist:
                return Response({"error": "User account does not exist."}, status=status.HTTP_404_NOT_FOUND)

            account.balance += amount
            account.save(update_fields=['balance'])
            transaction = Transaction.objects.create(account=account, amount=amount)

            email_subject = "Deposit Successful"
            email_body = render_to_string('deposit_email.html', {'amount' : amount, 'user': account})

            email = EmailMultiAlternatives(email_subject, '', to=[user.email])
            email.attach_alternative(email_body, "text/html")
            email.send()

            return Response({"message": f"BDT:{amount:.2f} deposited to your account successfully"}, status=status.HTTP_201_CREATED)
        
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class ReservationView(APIView):
    serializer_class = ReservationsSerializer
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            hotel = serializer.validated_data['hotel']
            package = serializer.validated_data['package']
            user = request.user

            try:
                hotel = Hotel.objects.get(id=hotel.id)
            except Hotel.DoesNotExist:
                return Response({"error": "Hotel not found."}, status=status.HTTP_404_NOT_FOUND)
            
            try:
                account = UserAccount.objects.get(user=user)
            except UserAccount.DoesNotExist:
                return Response({"error": "User account does not exist."}, status=status.HTTP_404_NOT_FOUND)


            if package == '1':
                amount = hotel.per_day_price
            elif package == '2':
                amount = hotel.per_day_price * 2
            elif package == '3':
                amount = hotel.per_day_price * 3
            else:
                return Response({"error": "Invalid package."}, status=status.HTTP_400_BAD_REQUEST)

        
            if account.balance < amount:
                return Response({"error": "Insufficient balance."}, status=status.HTTP_400_BAD_REQUEST)
            
            account.balance -= amount
            account.save(update_fields=['balance'])

            reservation = Reservations.objects.create(user=account, hotel=hotel, package = package)

            transaction = Transaction.objects.create(account=account, amount=amount)

            # send_reservation_notification(user, amount, 'Reservation Confirmation', 'reservation_email.html', hotel)
            
            email_subject = "Reservation Successful"
            email_body = render_to_string('reservation_email.html', {'amount' : amount, 'package' : package, 'user': account, 'hotel': hotel})

            email = EmailMultiAlternatives(email_subject, '', to=[user.email])
            email.attach_alternative(email_body, "text/html")
            email.send()


            return Response({"message": "Reservation successful."}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)