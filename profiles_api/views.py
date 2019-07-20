from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.

class HelloApiView(APIView):

    def get(self,request,formt=None):
        an_apiview = [
               'Uses Http method as function (get,post,patch,put,delete)',
               'Is similar to traditional django view',
               'gives you the most control over ypur logic',
               'IS mapped manually to urls',
        ]

        return Response({'message':'Hello!','an_apiview':an_apiview})
