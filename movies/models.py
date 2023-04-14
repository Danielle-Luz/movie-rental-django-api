from django.db import models


class RatingChoices(models.TextChoices):
    G = "G"
    PG = "PG"
    PG_13 = "PG-13"
    R = "R"
    NC_17 = "NC-17"


class Movie(models.Model):
    title = models.CharField(max_length=127)
    duration = models.CharField(max_length=10, null=True, default=None)
    rating = models.CharField(
        max_length=20, choices=RatingChoices.choices, null=True, default=RatingChoices.G
    )
    synopsis = models.TextField(null=True, default=None)
    user = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="movies"
    )


class MovieOrder(models.Model):
    price = models.DecimalField(decimal_places=2, max_digits=8)
    buyed_at = models.DateTimeField(auto_now_add=True)
    buyed_movie = models.ForeignKey(
        "movies.Movie", on_delete=models.CASCADE, related_name="movie_orders"
    )
    buyed_by = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="movie_orders"
    )
