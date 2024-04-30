
from django.shortcuts import render, redirect
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token

from . serializers import ClientSerializer, UserAccountSerializer, UserLoginSerializer
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode

from django.utils.encoding import force_bytes
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
from . models import UserAccount
# Create your views here.

class ClientViewset(viewsets.ModelViewSet):
    queryset = UserAccount.objects.all() 
    serializer_class = ClientSerializer


class UserRegistrationAPIView(APIView):
    serializer_class = UserAccountSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            default_token_generator.make_token(user)
            return Response("User registered successfully", status=201)
        return Response(serializer.errors, status=400)


    
    # previous code
    # serializer_class = UserAccountSerializer 
    # def post(self, request):
    #     serializer = self.serializer_class(data = request.data)
    #     if serializer.is_valid():
    #         user = serializer.save()
    #         print(f"User: {user}")
    #         token = default_token_generator.make_token(user)
    #         print(f"token: {token}")
    #         uid = urlsafe_base64_encode(force_bytes(user.pk))
    #         print(f"UID: {uid}")
    #         confirm_link = f"https://hotel-api-99rb.onrender.com/clients/active/{uid}/{token}"
    #         email_subject = "Confirm Your Email"
    #         email_body = render_to_string('confirm_email.html', {'confirm_link' : confirm_link})

    #         email = EmailMultiAlternatives(email_subject, '', to=[user.email])

    #         email.attach_alternative(email_body, "text/html")

    #         email.send()
    #         return Response("Check your mail for confirmation")
    #     return Response(serializer.errors)
    

# def activate(request, uid64, token):
#     try:
#         uid = urlsafe_base64_decode(uid64).decode()
#         user = User._default_manager.get(pk = uid)
#     except(User.DoesNotExist):
#         user = None

#     if user is not None and default_token_generator.check_token(user, token):
#         user.is_active = True
#         user.save()
#         return redirect('login')
    
#     else:
#         return redirect('register')
    


class UserLoginAPIView(APIView):
    def post(self, request):
        serializer = UserLoginSerializer(data=self.request.data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']
            print(username)
            print(password)
            
            user = authenticate(username=username, password=password)
            print(user)
           
            if user:
                token, create = Token.objects.get_or_create(user=user)
                login(request, user)
                print(token.key, user.id)
                return Response({'token': token.key, 'user_id': user.id})
            else:
                return Response({'error': "Invalid Credentials"})
        
        return Response(serializer.errors, status=400)


    # previous code
    # def post(self, request):
    #     serializer = UserLoginSerializer(data = self.request.data)
    #     if serializer.is_valid():
    #         username = serializer._validated_data['username']
    #         password = serializer._validated_data['password']

    #         user = authenticate(username = username, password = password)

    #         if user:
    #             token, create = Token.objects.get_or_create(user=user)
    #             login(request, user)
    #             return Response({'token': token.key, 'user_id': user.id})
    #         else:
    #             return Response({'error': "Invalid Credentials"})
        
    #     return Response(serializer.errors)



class UserLogoutView(APIView):
    def get(self, request):
        logout(request)
        return redirect('login')
        