from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserSerializer
from .models import User
from .permissions import UserInfoPermission
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated


class UserView(APIView):
    def post(self, request):
        validated_user = UserSerializer(data=request.data)

        try:
            validated_user.is_valid()

            validated_user.save()

            return Response(validated_user.data, status.HTTP_201_CREATED)
        except:
            return Response(validated_user.errors, status.HTTP_400_BAD_REQUEST)
        
class UserInfoView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [UserInfoPermission]

    def get(self, request, user_id):
        found_user = User.objects.get(id=user_id)

        self.check_object_permissions(request, found_user)

        user_serialized = UserSerializer(found_user).data

        try:
            return Response(user_serialized)
        except:
            return Response(user_serialized.errors, )


    def patch(self, request, user_id):
        user_to_update = User.objects.get(id=user_id)

        self.check_object_permissions(request, user_to_update)

        validated_new_user_info = UserSerializer(user_to_update, request.data, partial=True)
        validated_new_user_info.is_valid()

        updated_user =  validated_new_user_info.save()

        serialized_user = UserSerializer(updated_user).data

        return Response(serialized_user)