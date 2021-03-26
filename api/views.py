from django.http import request
from django.shortcuts import render, resolve_url
from rest_framework import viewsets
from rest_framework import permissions
from api.serializers import UserSerializer, MovieSerializer, CastSerializer
from django.contrib.auth.models import User
from netflix.models  import Movie, Cast

# from django.http import HttpResponse, JsonResponse
# from rest_framework.parsers import JSONParser
# from django.views.decorators.csrf import csrf_exempt
from rest_framework import status, generics
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
# Create your views here.


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class CastViewSet(viewsets.ModelViewSet):
    queryset = Cast.objects.all()
    serializer_class = CastSerializer
    permission_classes = [IsAuthenticated]

# @csrf_exempt
# def castListCreate(request):
#     if request.method == 'GET':
#         cast = Cast.objects.all()
#         serializer = CastSerializer(cast, many=True)
#         return JsonResponse(serializer.data, safe=False)

#     elif request.method == 'POST':
#         data =  JSONParser().parse(request)
#         serializer = CastSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=201)
#         return JsonResponse(serializer.errors, status=400)

# @csrf_exempt
# def castRetrieveUpdate(request, id):
#     try:
#         cast = Cast.objects.get(pk=id)
#     except Cast.DoesNotExist:
#         return HttpResponse(status=404)
    
#     if request.method == 'GET':
#         serializer = CastSerializer(cast)
#         return JsonResponse(serializer.data)

#     elif request.method == 'PUT':
#         data = JSONParser().parse(request)
#         serializer = CastSerializer(cast, data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data)
#         return JsonResponse(serializer.errors, status=400)
    
#     elif request.method == "DELETE":
#         cast.delete()
#         return HttpResponse({"success":"delete cast successfully"},status=204)



@api_view(['GET', 'POST'])
def castListCreate(request):
    if request.method == 'GET':
        cast = Cast.objects.all()
        serializer = CastSerializer(cast, many=True)
        return Response(serializer.data)

    elif request.method == 'POST' :
        serializer = CastSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
@permission_classes([IsAuthenticated,])
def castRetrieveUpdate(request, id):
    try:
        cast = Cast.objects.get(pk=id)
    except Cast.DoesNotExist:
        return Response(status= status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = CastSerializer(cast)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = CastSerializer(cast, data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        cast.delete()
        return Response(status= status.HTTP_204_NO_CONTENT)

class castGenericCR(generics.ListCreateAPIView):
    queryset = Cast.objects.all()
    serializer_class = CastSerializer

class castGenericRUD(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = "pk"
    queryset = Cast.objects.all()
    serializer_class = CastSerializer
    permission_classes = [IsAuthenticated]