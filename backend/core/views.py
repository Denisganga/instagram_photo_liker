from rest_framework.decorators import api_view
from rest_framework.response import Response
from .like_photos import like_photos  # Import the function here
import logging

logger = logging.getLogger(__name__)

@api_view(['POST'])
def like_photos_view(request):
    username = request.data.get('username')
    password = request.data.get('password')
    logger.info(f"Received credentials: {username}, {password}")  # Log received credentials
    result = like_photos(username, password)
    return Response({"status": "success", "details": result})
