from .serializers import MovieSerializer
from users.models import User

def get_movie_with_added_by(movie):
    owner_id = movie.user.id

    movie = MovieSerializer(movie).data

    found_user = User.objects.get(id=int(owner_id))
    found_user_email = found_user.email

    movie["added_by"] = found_user_email

    return movie