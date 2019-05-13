from rest_framework import serializers
from api.models import Status, Company, Position, UserInfo, UserApplication
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'#('id', 'username', 'first_name', 'last_name', 'email', 'password',)

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

class StatusSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True)

    def create(self, validated_data):
        status = Status(**validated_data)
        status.save()
        return status

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance


class CompanySerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True)

    def create(self, validated_data):
        company = Company(**validated_data)
        company.save()
        return company

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance


class PositionSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True)
    link = serializers.CharField(required=True)
    location = serializers.CharField(required=True)
    type = serializers.CharField(required=True)
    company = CompanySerializer(required=False)
    created_by = UserSerializer(required=False)

    class Meta:
        model = Position
        fields = '__all__'


class UserInfoSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserInfo
        fields = '__all__'


class UserApplicationSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    position = PositionSerializer()
    status = StatusSerializer()
    created_by = UserSerializer(required=False)

    class Meta:
        model = UserApplication
        fields = '__all__'



