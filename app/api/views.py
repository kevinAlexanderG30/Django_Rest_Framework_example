from rest_framework.viewsets import ModelViewSet
from app.models import Productos
from app.api.serializers import PostSerilizer

class PostApiViewSet(ModelViewSet):
    serializer_class = PostSerilizer
    queryset =Productos.objects.all()
