from rest_framework import serializers
from api.models import Status, Company, Position, User


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
    company = CompanySerializer()

    class Meta:
        model = Position
        fields = ('id', 'name', 'link', 'location', 'type', 'company',)


class UserSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    login = serializers.CharField(required=True)
    password = serializers.CharField(required=True)
    lastName = serializers.CharField(required=True)
    firstName = serializers.CharField(required=True)
    leetcodeUrl = serializers.CharField(required=True)

    class Meta:
        model = User
        fields = ('id', 'login', 'password', 'lastName', 'firstName', 'leetcodeUrl',)




