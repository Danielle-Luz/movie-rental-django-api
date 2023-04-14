from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Movie
from .utils import get_movie_with_added_by
from users.models import User
from .serializers import MovieSerializer, MovieOrderSerializer
from .permissions import EmployeePermission
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated


class MovieView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [EmployeePermission]

    def get(self, request):
        all_movies = [get_movie_with_added_by(movie) for movie in Movie.objects.all()]

        return Response(all_movies)

    def post(self, request):
        validated_movie = MovieSerializer(data=request.data)

        try:
            validated_movie.is_valid()

            created_movie = validated_movie.save(added_by=request.user)

            movie_with_added_by = get_movie_with_added_by(created_movie)

            return Response(movie_with_added_by, status.HTTP_201_CREATED)
        except:
            return Response(validated_movie.errors, status.HTTP_400_BAD_REQUEST)


class MovieInfoView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [EmployeePermission]

    def get(self, request, movie_id):
        try:
            found_movie = Movie.objects.get(id=movie_id)

            serialized_movie = get_movie_with_added_by(found_movie)

            return Response(serialized_movie)
        except:
            return Response(
                {"error": "movie not found"}, status=status.HTTP_404_NOT_FOUND
            )

    def delete(self, request, movie_id):
        try:
            found_movie = Movie.objects.get(id=movie_id)

            found_movie.delete()

            return Response(status=status.HTTP_204_NO_CONTENT)
        except:
            return Response(
                {"error": "movie not found"}, status=status.HTTP_404_NOT_FOUND
            )


class MovieOrderView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, movie_id):
        validated_order = MovieOrderSerializer(data=request.data)

        validated_order.is_valid()

        validated_order.validated_data["buyer_id"] = request.user.id
        validated_order.validated_data["movie_id"] = movie_id

        created_order = validated_order.save()

        return Response(created_order, status.HTTP_201_CREATED)
