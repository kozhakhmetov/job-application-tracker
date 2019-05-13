from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.http import Http404
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

from api.models import User, Company, Status
from api.serializers import StatusSerializer, PositionSerializer, UserSerializer, CompanySerializer


@api_view(['POST'])
def status(request):
    if request.method == 'POST':
        serializer = StatusSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


# @api_view(['DELETE'])
# def del_status(request, pk):
#    try:
#         stat = Status.objects.get(id=pk)
#    except  Status.DoesNotExist as e:
#        return Response({'error': str(e)}, status=status.HTTP_404_NOT_FOUND)
#    stat.delete()
#    return Response({}, status=status.HTTP_204_NO_CONTENT)


@api_view(['POST'])
def position(request):
    if request.method == 'POST':
        serializer = PositionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(created_by=request.user, company=request.company)
            return Response(serializer.data)
        return Response(serializer.errors)


class CompanyView(APIView):
    def get_object(self, pk):
        try:
           return Company.objects.get(id=pk)
        except Company.DoesNotExist:
           raise Http404

    def get(self, request, pk):
        company = self.get_object(pk)
        serializer = CompanySerializer(company)
        return Response(serializer.data)

    def post(self, request):
        serializer = CompanySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(created_by=self.request.user)
            return Response(serializer.data)
        return Response(serializer.errors)

    def put(self, request, pk):
        company = self.get_object(pk)
        serializer = CompanySerializer(instance=company, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request, pk):
        company = self.get_object(pk)
        company.delete()
        return Response({})

