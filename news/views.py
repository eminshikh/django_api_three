from rest_framework.response import Response
from rest_framework.views import APIView
from .models import ThreeNews
from .serializers import ThreeNewsSerializer

class ThreeNewsList(APIView):
    def get(self, request):
          queryset = ThreeNews.objects.all()
          serializer = ThreeNewsSerializer(queryset, many=True)
          return Response({'news': serializer.data})
