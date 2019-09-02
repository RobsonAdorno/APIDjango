from rest_framework.viewsets import ModelViewSet

from RestDjango.product.api.serializers import ProductSerializer
from RestDjango.product.models import Product


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

