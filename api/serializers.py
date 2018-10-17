from rest_framework import serializers
from items.models import Item, FavoriteItem
from django.contrib.auth.models import User 

class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = [ 'first_name' , 'last_name']


class FavoriteItemSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = FavoriteItem
        fields = ['user']

class ItemListSerializer(serializers.ModelSerializer):
	detail = serializers.HyperlinkedIdentityField(
		view_name = "api-detail",
		lookup_field = "id",
		lookup_url_kwarg = "item_id",
		)
	added_by = UserSerializer()
	like_count = serializers.SerializerMethodField()
	class Meta:
		model = Item
		fields = [
			'name',
			'image',
			'added_by',
			'detail',
			'like_count'
			]
	def get_like_count(self, obj):
		count = obj.favoriteitem_set.count()
		return count


class ItemDetailSerializer(serializers.ModelSerializer):

	users = serializers.SerializerMethodField()
	class Meta:
		model = Item
		fields = [
			'name',
			'image',
			'description',
			'users'
			]
	def get_users(self, obj):
		items = obj.favoriteitem_set.all()
		return FavoriteItemSerializer(items, many=True).data
