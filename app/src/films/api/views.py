from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.db.models import Avg

from ..models import Film
from .serializers import FilmSerializer


@api_view(['GET', 'POST'])
def main_page(request):
    if request.method == 'GET':
        data = Film.objects.all().annotate(
            rate=(
                Avg('userfilmrelation__rate')
            )
        ).select_related('category')
        serializer_data = FilmSerializer(data, many=True).data
        return Response(serializer_data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        try:
            data = request.data 
            serializer_data = FilmSerializer(data=data)
            if serializer_data.is_valid():
                serializer_data.save()
                return Response(serializer_data, status=status.HTTP_201_CREATED)
        except Exception as e:
            print(e)
            return Response({
                'data': {},
                'message': 'something wrong..'
            }, status=status.HTTP_400_BAD_REQUEST)