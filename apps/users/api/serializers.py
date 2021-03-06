from rest_framework import serializers
from apps.users.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
    
    def create(self, validated_data):
        user = User(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

    def update(self, instance, validated_data):
        user_update= super().update(instance, validated_data) 
        user_update.set_password(validated_data['password'])
        user_update.save()
        return user_update

   

class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User

    def to_representation(self, instance):
        return {
            'id' : instance['id'],
            'username' : instance['username'],
            'email' : instance['email'],
            'password' : instance['password']
        }