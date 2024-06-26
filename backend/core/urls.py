from django.urls import path
from .views import like_photos_view

urlpatterns = [
    path('like-photos/', like_photos_view, name='like_photos'),
]
