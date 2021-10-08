from rest_framework import serializers
from authentication.models import CustomUser
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password


class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required = True,
        validators = [UniqueValidator(queryset=CustomUser.objects.all())]
    )

    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    confirm_password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = CustomUser
        fields  = ['email', 'password', 'confirm_password', 'username']

    
    def validate(self, attrs):
        if attrs['password'] != attrs['confirm_password']:
            raise serializers.ValidationError({'password': 'password do not match'})
        
        return attrs

    
    def create(self, validated_data):
        user = CustomUser.objects.create(
            username = validated_data['username'],
            email = validated_data['email']
        )

        user.set_password(validated_data['password'])
        user.save()
        return user


