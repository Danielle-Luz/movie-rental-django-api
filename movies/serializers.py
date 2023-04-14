from rest_framework import serializers
from .models import Movie, RatingChoices
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
    
