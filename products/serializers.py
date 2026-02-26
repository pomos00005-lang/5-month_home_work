from rest_framework import serializers
from .models import Category,Product,Review



class CategoryListSeializers(serializers.ModelSerializer):
    class Meta():
        model = Category
        fields = 'name'.split()

class CategoryDetailSeializers(serializers.ModelSerializer):
    class Meta():
        model = Category
        fields = '__all__'



class ProductListSerializer(serializers.ModelSerializer):
    class Meta():
        model = Product
        fields = 'title price'.split()

class ProductDetailSerializer(serializers.ModelSerializer):
    class Meta():
        model = Product
        fields = '__all__'



class ReviewListSerializers(serializers.ModelSerializer):
    class Meta():
        model = Review
        fields = 'text product'.split()

class ReviewDetailSerializers(serializers.ModelSerializer):
    class Meta():
        model = Review
        fields = '__all__'