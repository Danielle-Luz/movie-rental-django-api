from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserSerializer


class UserView(APIView):
    def post(self, request):
        validated_user = UserSerializer(data=request.data)

        try:
            validated_user.is_valid()

            validated_user.save()

            return Response(validated_user.data, status.HTTP_201_CREATED)
        except:
            return Response(validated_user.errors, status.HTTP_400_BAD_REQUEST)
