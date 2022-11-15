from .serializers import ProductSerializer
from rest_framework import generics as gc
from .models import Product

class ProductView(gc.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
