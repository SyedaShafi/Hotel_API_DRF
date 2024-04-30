from rest_framework import serializers
from .models import Transaction

class UserTransactionSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(many=False)
    class Meta:
        model = Transaction
        fields = '__all__'


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ['amount']

    def validate_amount(self, value):
        if value <= 1000:
            raise serializers.ValidationError(f"Amount must be greater than 1000.")
        return value

    # def create(self, validated_data):
    #     account = validated_data['account']
    #     amount = validated_data['amount']
    #     account.balance += amount
    #     account.save()
    #     transaction = Transaction.objects.create(account=account, amount=amount)
    #     return transaction
    
    def update(self, instance, validated_data):
        raise NotImplementedError("Transaction updates are not supported.")


PACKAGE_TYEP = (
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
)

# class ReservationRequestSerializer(serializers.Serializer):
#     hotel_id = serializers.IntegerField()
#     package = serializers.ChoiceField(choices=PACKAGE_TYEP)