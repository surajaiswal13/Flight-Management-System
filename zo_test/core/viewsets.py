from .serializers import UserSerializer, UserSerializerTwo
from .models import UserTest
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

class UserViewSet(viewsets.ModelViewSet):

    queryset = UserTest.objects.all()
    serializer_class = UserSerializer

    def get_serializer_class(self):
        if self.action == 'list':
            return UserSerializerTwo
        if self.action == 'retrieve':
            return UserSerializerTwo
        return UserSerializer

    @action(detail=True, methods=['post'])
    def get_data(self, request):
        
            return Response({'status': 'password set'})
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)