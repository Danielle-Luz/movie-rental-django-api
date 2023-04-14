from rest_framework import serializers
from .models import Movie, RatingChoices, MovieOrder
from users.models import User


class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=127, required=True)
    duration = serializers.CharField(max_length=10, required=False)
    rating = serializers.ChoiceField(choices=RatingChoices.choices, required=False)
    synopsis = serializers.CharField(required=False)

    def create(self, validated_data: dict):
        added_by = validated_data.pop("added_by")

        validated_data["user"] = added_by

        created_movie = Movie.objects.create(**validated_data)

        return created_movie


class MovieOrderSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.SerializerMethodField(read_only=True)
    price = serializers.DecimalField(decimal_places=2, max_digits=8)
    buyed_at = serializers.DateTimeField(read_only=True)
    buyed_by = serializers.SerializerMethodField(read_only=True)

    def get_title(self, obj):
        buyed_movie = Movie.objects.get(obj.buyed_movie.id)
        movie_title = buyed_movie.title

        return movie_title

    def get_buyed_by(self, obj):
        buyed_by = User.objects.get(obj.buyed_by.id)
        buyer_email = buyed_by.email

        return buyer_email
    
    def create(self, validated_data: dict):
        buyer_id = validated_data.pop("buyer_id")
        buyed_movie_id = validated_data.pop("movie_id")

        found_buyer = User.objects.get(id=buyer_id)
        found_movie = Movie.objects.get(id=buyed_movie_id)

        validated_data["buyed_by"] = found_buyer
        validated_data["buyed_movie"] = found_movie

        created_order = MovieOrder.objects.create(**validated_data)

        return created_order



