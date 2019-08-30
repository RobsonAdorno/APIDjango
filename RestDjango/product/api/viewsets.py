from rest_framework.viewsets import ModelViewSet
from ..models import Product
from ..api.serializers import ProductSerializer


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
