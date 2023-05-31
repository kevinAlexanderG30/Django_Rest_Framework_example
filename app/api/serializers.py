from rest_framework.serializers import ModelSerializer
from app.models import Productos

class PostSerilizer(ModelSerializer):
    class Meta:
        model = Productos
        fields = ['id', 'nombre', 'precio', 'descripcion']