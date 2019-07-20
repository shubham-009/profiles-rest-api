from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from profiles_api import serializers

from rest_framework import viewsets
# Create your views here.

class HelloApiView(APIView):

    serializer_class = serializers.HelloSerializer

    def get(self,request,formt=None):
        an_apiview = [
               'Uses Http method as function (get,post,patch,put,delete)',
               'Is similar to traditional django view',
               'gives you the most control over ypur logic',
               'IS mapped manually to urls',
        ]

        return Response({'message':'Hello!','an_apiview':an_apiview})


    def post(self,request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message':message})

        else:
            return Response(serializer.errors,status.HTTP_400_BAD_REQUEST)

    def put(self,request,pk=None):
        return Response({'method':'PUT'})

    def patch(self,request,pk=None):
        return Response({'method':'patch'})

    def delete(self,request,pk=None):
        return Response({'method':'delete'})



class HelloViewSet(viewsets.ViewSet):
    serializer_class = serializers.HelloSerializer
    def list(self,request):
        a_viewset=[
              'Uses action (list,create,update,retrieve,partial_update)',
              'Automatically maps to url using router',
              'Provides more functionality in less code',
        ]

        return Response({'message':'hello','a_viewset':a_viewset})


    def create(self,request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message':message})

        else:
            return Response(serializer.errors,status.HTTP_400_BAD_REQUEST)

    def retrieve(self,request,pk=None):
        return Response({'http_method':'GET'})

    def update(self,request,pk=None):
        return Response({'http_method':'PUT'})

    def partial_update(self,request,pk=None):
        return Response({'http_method':'PATCH'})

    def destroy(self,request,pk=None):
        return Response({'http_method':'DELETE'})
