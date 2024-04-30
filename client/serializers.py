from rest_framework import serializers
from django.contrib.auth.models import User
from . import models
from . constants import GENDER_TYPE



class ClientSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(many=False)
    class Meta:
        model = models.UserAccount
        fields = '__all__'



class UserAccountSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(required = True)
    birth_date = serializers.DateField(allow_null=True, required=False)
    gender = serializers.ChoiceField(choices=GENDER_TYPE)
    phone = serializers.CharField(max_length=30)
  
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password', 'confirm_password', 'gender', 'birth_date', 'phone' ]
    
    def save(self):
        username = self.validated_data['username']
        first_name = self.validated_data['first_name']
        last_name = self.validated_data['last_name']
        email = self.validated_data['email']
        password = self.validated_data['password']
        password2 = self.validated_data['confirm_password']
        gender = self.validated_data['gender']
        birth_date = self.validated_data['birth_date']
        phone = self.validated_data['phone']
        balance = 0

        if password != password2:
            raise serializers.ValidationError({'error': 'Password does not match.'})
        
        if User.objects.filter(email = email).exists():
            raise serializers.ValidationError({'error': 'Email already exists.'})
    
        
        account = User.objects.create(username = username, first_name = first_name, last_name=last_name, email = email)

        user_account = models.UserAccount.objects.create(user = account, birth_date = birth_date, gender=gender, phone=phone, balance = balance)

        account.set_password(password)
        print(account)
        account.save()
        user_account.save()
        return account


class UserLoginSerializer(serializers.Serializer):
    username =serializers.CharField(required = True)
    password =serializers.CharField(required = True)
    