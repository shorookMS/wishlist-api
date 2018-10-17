from items.models import Item
from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    RetrieveUpdateAPIView,
    DestroyAPIView,
    CreateAPIView,

)
from .serializers import ItemListSerializer, ItemDetailSerializer
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from .permissions import IsOwner
# Create your views here.
class ItemListView(ListAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemListSerializer
    filter_backends = [OrderingFilter, SearchFilter]
    permission_classes = [AllowAny,]
    search_fields = ['name', 'description']


class ItemDetailView(RetrieveAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemDetailSerializer
    permission_classes = [IsOwner,]
    lookup_field = 'id'
    lookup_url_kwarg = 'item_id'
